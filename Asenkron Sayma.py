# asyncio modülünü içe aktarıyoruz, bu modül asenkron programlama için kullanılır.
import asyncio

# 'count' adında asenkron bir fonksiyon tanımlıyoruz.
async def count():
    print("Bir")  # "Bir" yazdırıyoruz.
    await asyncio.sleep(1)  # Asenkron olarak 1 saniye bekliyoruz. Bu süre boyunca diğer asenkron işlemler çalışabilir.
    print("İki")  # Bekleme süresi sona erdikten sonra "İki" yazdırıyoruz.

# 'main' adında başka bir asenkron fonksiyon tanımlıyoruz.
async def main():
    # 'asyncio.gather' kullanarak, 'count' fonksiyonunun 3 farklı örneğini aynı anda çalıştırıyoruz.
    # Bu sayede, her 'count' çağrısı birbirinden bağımsız olarak ve paralel bir şekilde işlenebilir.
    await asyncio.gather(count(), count(), count())

# Programımızın asenkron 'main' fonksiyonunu çalıştırıyoruz.
asyncio.run(main())
