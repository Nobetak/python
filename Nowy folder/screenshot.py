from datetime import datetime
import time

import pyscreenshot as IMGgrab
import schedule


def take_screenshot():
    print("taking a screenshot")
    image_name = f"screenshot-{datetime.now().strftime('%d_%H-%M')}"
    screenshot = IMGgrab.grab()

    filepath = f"./screenshot/{image_name}.png"

    screenshot.save(filepath)
    print("screenshot taken")
    return filepath


def main():
    schedule.every(5).seconds.do(take_screenshot)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
