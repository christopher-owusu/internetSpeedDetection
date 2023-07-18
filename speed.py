import speedtest                 #pip install speedtest-cli

def speed():
    print('Calculating speed.........')
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Perform the speed test
    download_speed = st.download()  # Measured download speed in bits per second
    upload_speed = st.upload()  # Measured upload speed in bits per second

    # Convert speeds to a more readable format
    download_speed_mbps = download_speed / 1000000  # Convert to megabits per second
    upload_speed_mbps = upload_speed / 1000000  # Convert to megabits per second

    # Print the results
    print(f"Download speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload speed: {upload_speed_mbps:.2f} Mbps")

    print('Done processing.')

speed()