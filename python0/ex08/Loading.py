import time
from shutil import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """
    This function takes a range object and prints a progress bar
    with timing similar to tqdm
    """
    block = '\u2588'
    total = len(lst)
    terminal_width = (get_terminal_size().columns / 4) * 3.08
    start_time = time.time()
    last_print_time = start_time
    min_update_interval = 0.1

    for i in lst:
        current_time = time.time()
        time_diff = current_time - last_print_time
        if time_diff >= min_update_interval or i == total - 1:
            tt = int((i + 1) / total * terminal_width)
            elapsed_time = current_time - start_time
            percentage = int((i + 1) / total * 100)
            progress_bar = f'\r{percentage}%|{block * tt}'
            progress_bar += ' ' * (int(terminal_width) - tt) + '|'
            speed = (i + 1) / elapsed_time if elapsed_time > 0 else 0
            remaining_time = (total - (i + 1)) / speed if speed > 0 else 0
            elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed_time))
            remaining_str = time.strftime("%M:%S", time.gmtime(remaining_time))
            time_info = f"[{elapsed_str}<{remaining_str}, {speed:.2f}it/s]"
            print(f'\r{progress_bar} {i + 1}/{total} {time_info}', end="")
            last_print_time = current_time
        yield i
    print()
