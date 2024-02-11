### EXAMPLE
import requests
import json
from time import sleep

def sendRequestNoContext(text, model_a, userlist, id):
  user = findUser(id, userlist)
  model = model_a[0]
  model_price = model_a[1]
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer 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",
      "HTTP-Referer": f"telegram.org",
      "X-Title": f"AS1MOV",
    },
    data = json.dumps({
      "model": model,
      "messages": [
        {"role": "user", "content": text}
      ]
    })
  )
  resp_dict = response.json()
  op = 'RESPONSE: '
  temptext = "https://openrouter.ai/api/v1/generation?id="
  temptext += resp_dict["id"]
  a1 = requests.get(url=temptext, headers={'Authorization': f'Bearer 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'})
  a2 = a1.json()
  a3 = a2['data']
  a4 = a3['native_tokens_prompt']
  a41 = a3['native_tokens_completion']
  tokens_used = a4 + a41
  credits_used = tokens_used * model_price
  rp1 = resp_dict["choices"]
  rp2 = rp1[0]
  rp3 = rp2["message"]
  rp4 = rp3["content"]
  op += rp4
  usercred = user[1]
  usercred -= credits_used
  user[1] = usercred
  print(user)
  op += rp4
  return op, userlist, tokens_used

def SendRequest(text, model):
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer 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",
      "HTTP-Referer": f"telegram.org",
      "X-Title": f"AS1MOV",
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



# print(SendRequest('Бесцветные зелёные идеи яростно спят', 'gryphe/mythomist-7b:free'))



file1 = open('test1.txt', 'r', encoding="utf-8")
filegpt = open('t1-gpt35.txt', 'a', encoding='utf-8')
filellama = open('t1-llama13b.txt', 'a', encoding='utf-8')
filemistral = open('t1-mistral.txt', 'a', encoding='utf-8')
f1a = file1.read()
f1b = f1a.split('\n')
# GPT-3.5
print('GPT-3.5 TESTING...')
print('---------------')
for i in range(len(f1b)):
  ap = f1b[i]
  ab = SendRequest(ap, 'openai/gpt-3.5-turbo-0125')
  filegpt.write(ab)
  filegpt.write('\n')
  filegpt.close()
  filegpt = open('t1-gpt35.txt', 'a', encoding='utf-8')
  print('Sentence No.', i, 'translated successfully!')
  sleep(2)
# LLaMa-13B
print('LLAMA TESTING...')
print('---------------')
for i in range(len(f1b)):
  ap = f1b[i]
  ab = SendRequest(ap, 'meta-llama/llama-2-13b-chat')
  filellama.write(ab)
  filellama.write('\n')
  filellama.close()
  filellama = open('t1-llama13b.txt', 'a', encoding='utf-8')
  print('Sentence No.', i, 'translated successfully!')
  sleep(1)
# Mistral
print('MISTRAL TESTING...')
print('---------------')
for i in range(len(f1b)):
  ap = f1b[i]
  ab = SendRequest(ap, 'teknium/openhermes-2.5-mistral-7b')
  filemistral.write(ab)
  filemistral.write('\n')
  filemistral.close()
  filemistral = open('t1-mistral.txt', 'a', encoding='utf-8')
  print('Sentence No.', i, 'translated successfully!')
  sleep(1)


# Первый крупномасштабный тест

