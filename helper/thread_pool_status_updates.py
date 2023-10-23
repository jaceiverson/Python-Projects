import warnings
from concurrent.futures import ThreadPoolExecutor
from typing import Callable

import requests
from rich import print
from tqdm import tqdm


class ThreadTracker:
    def __init__(
        self,
        function_to_run: Callable = None,
        function_params: list = None,
        call_back_url: str = None,
        thread_workers: int = 10,
        progress_update_interval: int = 5,
    ) -> None:
        """
        :param function_to_run: the function to run in parallel
        :param function_params: the list of parameters to pass to the function
        :param call_back_url: the url to call back to
        :param thread_workers: the number of threads to run
        :param progress_update_interval: how often to update the progress bar
        """
        self.function_to_run = function_to_run
        self.function_params = function_params
        self.callback_url = call_back_url
        self.thread_workers = thread_workers
        self.progress_update_interval = progress_update_interval
        self.live_progress = 0
        self.show_output = False

    def output_results(self, show_output: bool = True) -> None:
        """
        call this method with False to hide print statements in run
        call this method with True to show print statements in run
        """
        self.show_output = show_output

    def set_workers(self, thread_workers: int) -> None:
        """
        Set the number of threads to run
        """
        self.thread_workers = thread_workers

    def set_progress_update_interval(self, interval: int) -> None:
        """
        Set the progress update interval in seconds
        """
        self.progress_update_interval = interval

    def set_callback_url(self, url: str) -> None:
        """
        Set the callback url to send the progress to
        """
        self.callback_url = url

    def clean_live_progress(self) -> str:
        """
        Round progress number and convert to be a string"""
        return str(round(self.live_progress * 100))

    def update_process(self, new_progress: float) -> None:
        """
        Update the progress if it has changed,
        make callback,
        and print progress if show_output is True
        """
        # our API call would happen here instead of printing
        if self.live_progress != new_progress:
            self.live_progress = new_progress
            # callback
            self.callback()
            if self.show_output:
                print(f"PROGRESS: {self.clean_live_progress()}")

    def callback(self) -> None:
        """
        send a http post request with how far along the process bar is
        """
        if self.callback_url is not None:
            requests.post(
                self.callback_url,
                json={
                    "progress": self.clean_live_progress(),
                    "function_name": self.function_to_run.__name__,
                    "file_path": __file__,
                },
                headers={"Content-Type": "application/json"},
            )

    def run(self, function_name: Callable = None, function_params: list = None) -> list:
        """
        Run the function in parallel
        :param function_name: the function to run in parallel - will overwrite the self.function_to_run attribute
        :param function_params: list of parameters for our function - will overwrite the self.function_params attribute
        :return: the results of the function_name or self.function_to_run
        """
        # check if we have a callback url, warn if not
        if self.callback_url is None:
            warnings.warn(
                UserWarning(
                    "No callback url set. Thread will run, updates will not be sent."
                )
            )

        # see if we have any passed in params that will overwrite our class attributes locally for this run
        if function_name is None:
            function_name = self.function_to_run
        if function_params is None:
            function_params = self.function_params
        with ThreadPoolExecutor(max_workers=self.thread_workers) as p:
            # results = list(tqdm(p.map(_foo, range(max_)), total=max_))
            results = []
            with tqdm(
                total=len(function_params), mininterval=self.progress_update_interval
            ) as pbar:
                for function_result in p.map(function_name, function_params):
                    results.append(function_result)
                    pbar.update()
                    # update the progress callback
                    self.update_process(pbar.last_print_n / pbar.total)
        # process completion
        self.update_process(1)
        return results
