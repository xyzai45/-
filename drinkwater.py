import time
from plyer import notification  # 需要安装 plyer 模块

def remind_to_drink_water():
    # 设置提醒间隔（以秒为单位）
    reminder_interval = 1800  # 30分钟

    while True:
        # 发送提醒
        notification.notify(
            title='喝水提醒',
            message='记得喝水哦！',
            app_icon=None,  # 如果有图标，可以在这里设置
            timeout=10,  # 提醒显示的时间（秒）
        )

        # 等待一定时间后再次提醒
        time.sleep(reminder_interval)

if __name__ == "__main__":
    remind_to_drink_water()
