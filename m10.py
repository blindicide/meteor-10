### EXAMPLE
import requests
import together
import json
import time
import asyncio
from vars import OR_key, TAI_key, gpt35, llama, mistral, ygpt1, ygpt2
together.api_key = TAI_key
folder_id = 'b1gi9uaaq775kkgub8hp'
yandexgpt_key = ygpt1
yandex_gpt_api_url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'


def SendRequestOR(text, model, key):
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": key,
      "HTTP-Referer": f"NONE",
      "X-Title": f"METEOR-10",
    },
    data = json.dumps({
      "model": model,
      "messages": [
        {"role": "system", "content": "Output the English translation of the following message. Nothing more."},
        {"role": "user", "content": text}
      ]
    })
  )
  resp_dict = response.json()
  rp1 = resp_dict["choices"]
  rp2 = rp1[0]
  rp3 = rp2["message"]
  rp4 = rp3["content"]
  return rp4




def SendRequestYGPT(text):
    YGPT_messages = [
    {
        "role": "system",
        "text": "Ты - продвинутый переводчик на основе ИИ. Тебе нужно перевести следующее предложение на английский:"
    },
    {
      "role": "user",
      "text": text,
    }
    ]
    response = requests.post(
        yandex_gpt_api_url,
        headers={
            "Authorization": f"Api-Key {yandexgpt_key}",
            "x-folder-id": folder_id
        },
        json={
            "modelUri": f"gpt://{folder_id}/yandexgpt/latest",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6
            },
            "messages": YGPT_messages
        },
    )
    resp_dict = response.json()
    print(resp_dict)
    rp1 = resp_dict["result"]
    rp2 = rp1['alternatives']
    rp3 = rp2[0]
    rp4 = rp3["message"]
    rp5 = rp4['text']
    return rp5



# print(SendRequestOR('Бесцветные зелёные идеи яростно спят', 'gryphe/mythomist-7b:free'))


def run_translation_OR(model, file, inpt, sleeptime):
  output = open(file, 'a', encoding='utf-8')
  global OR_key
  totaltime = 0
  for i in range(len(inpt)):
    sentence = inpt[i]
    if len(sentence) > 5:
      time1 = time.time()
      out = SendRequestOR(sentence, model, OR_key)
      output.write(out)
      output.write('\n')
      output.close()
      output = open(file, 'a', encoding='utf-8')
      time2 = time.time()
      totaltime += (time2 - time1)
      print('Line No.', i, 'served in', str(time2 - time1), 'seconds.')
      time.sleep(sleeptime)
    else:
      pass
  print('Total time for', len(inpt), 'requests is', totaltime, 'seconds.')
  output.close()


def run_translation_Yandex(file, inpt, sleeptime):
  totaltime = 0
  output = open(file, 'a', encoding='utf-8')
  for i in range(len(inpt)):
    sentence = inpt[i]
    if len(sentence) > 5:
      time1 = time.time()
      out = SendRequestYGPT(sentence)
      output.write(out)
      output.write('\n')
      output.close()
      output = open(file, 'a', encoding='utf-8')
      time2 = time.time()
      totaltime += (time2 - time1)
      print('Line No.', i, 'served in', str(time2 - time1), 'seconds.')
      time.sleep(sleeptime)
    else:
      pass
  print('Total time for', len(inpt), 'requests is', totaltime, 'seconds.')




file1 = open('test2.txt', 'r', encoding="utf-8")
filegpt = open('t1-gpt35.txt', 'a', encoding='utf-8')
filellama = open('t1-llama13b.txt', 'a', encoding='utf-8')
filemistral = open('t1-mistral.txt', 'a', encoding='utf-8')
fileyandex = open('t1-ygpt.txt', 'a', encoding='utf-8')
f1a = file1.read()
f1b = f1a.split('\n')

# GPT-3.5
print('GPT-3.5 TESTING...')
print('---------------')
run_translation_OR(gpt35, 't1-gpt35.txt', f1b, 0.1)
# LLaMa-13B
print('LLAMA TESTING...')
print('---------------')
run_translation_OR(llama, 't1-llama13b.txt', f1b, 0.1)
# Mistral
print('MISTRAL TESTING...')
print('---------------')
run_translation_OR(mistral, 't1-mistral.txt', f1b, 0.1)
print('YGPT TESTING...')
run_translation_Yandex('t1-ygpt.txt', f1b, 0.1)




# Первый крупномасштабный тест

