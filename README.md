
# EFSANE USERBOT

### Botu Kurmanın Kolay Yolu
APP ID ve API HASH'ı şuradan alın: [HERE](https://telegram.dog/OtoMyTelegramBot) ve BOT TOKEN buradan [Bot Father](https://t.me/botfather) ve Ardından Aşağıdaki Butona  Basarak StringSession Alınız. Stringinizi Aldıktan sonra Aşağıda Pembe Heroku Butonuna Basıp Deploy İşlemini Başlatınız

[![Get string session](https://repl.it/badge/github/brsitolmyers/exelonstringalici)](https://exelonstringalici.bristolmyers.repl.run/)

<a href="https://heroku.com/deploy?template=https://github.com/Mehmetbaba06/EfsaneStarBot"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-red?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p> 

<p align="center">
  <a href="https://github.com/BristolMyers/ExelonUserBot/fork">

<img src="https://i.ibb.co/syVTfWb/6d58817f09e15d326fa1807f2a57587c.jpg" alt="6d58817f09e15d326fa1807f2a57587c" border="0"> 
  </a>
  <a href="https://github.com/Mehmetbaba06/EfsaneStarBot">

  </a>
</p>


### Güncellemeler için [buraya](https://t.me/ExelonUserBot) tartışma ve hatalar için [buraya](https://t.me/ExelonSupport) katılın.

### Normal Yol

Örnek bir `local_config.py` dosyası şöyle olabilir:

**Tüm değişkenler zorunlu değildir**

__Userbot, yalnızca ilk iki değişkeni ayarlayarak çalışmalıdır__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Yapılandırması



**Heroku Yapılandırması**
Yapılandırmayı olduğu gibi bırakın.

**Local Yapılandırma**

Neyse ki UniBorg Destek Yapılandırması için zorunlu değişkenler yoktur.

## Zorunlu Değişkenler

- Ortam değişkenlerinden yalnızca ikisi zorunludur.
- Bunun nedeni `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   Bu değeri şuradan alabilirsiniz: https://telegram.dog/OtoMyTelegramBot
    - `API_HASH`:   Bu değeri şuradan alabilirsiniz: https://telegram.dog/OtoMyTelegramBot
- Exelon zorunlu değişkenleri ayarlamadan çalışmayacaktır.
