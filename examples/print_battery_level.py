from pyomyo import Myo, emg_mode

def battery_handler(battery_level):
    print(f"Battery Level: {battery_level}%")

# Initialize Myo connection
m = Myo(mode=emg_mode.NO_DATA)
m.connect()

# Add battery handler
m.add_battery_handler(battery_handler)

try:
    while True:
        m.run()
except KeyboardInterrupt:
    m.disconnect()
    quit()