from flask import Flask, request, jsonify # type: ignore
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory # type: ignore

app = Flask(__name__)

# Buat objek stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillment_text = "Maaf, saya tidak mengerti."

    if req.get("queryResult"):
        query_result = req.get("queryResult")
        user_input = query_result.get("queryText")
        
        # Melakukan stemming pada input pengguna
        stemmed_input = stemmer.stem(user_input)
        
        # Tanggapan berdasarkan kata dasar dari input pengguna
        if 'alamat' in stemmed_input:
            fulfillment_text = "Toko beroperasional pukul 07.00 hingga 21.00 di Jalan Pulo Wonokromo No.304, Wonokromo, Kota Surabaya, Jawa Timur 60241, Indonesia dan sayangnya umkm hafidz pigura belum memiliki cabang toko ditempat lainnya."
        elif 'harga' in stemmed_input:
            fulfillment_text = "Harga pigura dimulai dari 15.000 dan harga pigura custom menyesuaikan dengan ukuran yang anda inginkan"
        elif 'pengiriman' in stemmed_input:
            fulfillment_text = "Pengiriman produk umkm hafidz pigura bisa melalui ojek online baik grab, gojek, atau yang lainnya, hafidz pigura bisa mengirim ke luar kota menggunakan layanan jasa ekspedisi yang ada."
        elif 'ukuran' in stemmed_input:
            fulfillment_text = "Saat ini kami memiliki ketersedian ukuran pigura a4, a3n, dan kami menyediakan jasa custom ukuran dan bentuk pigura sesuai kebutahan anda"

    response = {
        "fulfillmentText": fulfillment_text
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

