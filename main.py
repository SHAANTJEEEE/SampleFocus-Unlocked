import os
import requests
import json
from bs4 import BeautifulSoup
from colorama import Fore

download_folder = 'SampleFocus Exported'

print(f'{Fore.LIGHTWHITE_EX}SampleFocus Unlocked 1.0.4\nMade by werxqq0\n{Fore.LIGHTCYAN_EX}https://github.com/werxqq0/SampleFocus-Unlocked\n')

while True:
    input_audio_link = input(f'{Fore.LIGHTWHITE_EX}Audio Link: ')

    def download_audio(link):
        if link.startswith('https://samplefocus.com/'):
            os.makedirs(download_folder, exist_ok=True)
            def download_audio_system(link):
                response = requests.get(link)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    sample_waveform_div = soup.find('div', {'data-react-class': 'SampleWaveform'})

                    if sample_waveform_div:
                        data_react_props = sample_waveform_div.get('data-react-props')

                        props_json = json.loads(data_react_props)

                        audio_link = props_json.get('sample').get('sample_mp3_url')
                if audio_link:
                            file_name = os.path.basename(f'{input_audio_link}.mp3')
                            file_name = file_name.replace("-", " ").title()
                            file_path = os.path.join(download_folder, file_name)

                            response = requests.get(audio_link)
                            if response.status_code == 200:
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)
                                print(f'{Fore.LIGHTGREEN_EX}File «{file_name}» downloaded successfully.\n')
                            else:
                                print(f'{Fore.LIGHTRED_EX}Cannot download file «{file_name}»!\n')
                        else:
                            print(f'{Fore.LIGHTRED_EX}Could not find a link to download audio on the page!\n')
                    else:
                        print(f'{Fore.LIGHTRED_EX}The download element could not be found on the page!\n')
                else:
                    print(f'{Fore.LIGHTRED_EX}This audio does not exist!\n')

            download_audio_system(input_audio_link)
        else:
            print(f'{Fore.LIGHTRED_EX}This link is not a SampleFocus site!\n')
            return False

    download_audio(input_audio_link)
