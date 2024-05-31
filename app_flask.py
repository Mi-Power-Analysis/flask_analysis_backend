from flask import Flask, request, jsonify

app = Flask(__name__)
data = {
  "analysis": [
    {
      "title" : "Kategorik Değişken Analizi",
      "results" : [
        {
      "title": "Kategorik Değişkenler",
      "description": "Kategorik Değişkenler resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Kategorik%20Degiskenler/ilk%20inceleme/fjn7jdtpxzbxk2ne6zjg.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Kategorik%20Degiskenler/ilk%20inceleme/lpov1xv9t5jjk8kzm6jq.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Kategorik%20Degiskenler/ilk%20inceleme/znfnrxmpl7nreaeenrfg.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Kategorik%20Degiskenler/ilk%20inceleme/axygccnh2ptlpxm4pypo.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Kategorik%20Degiskenler/ilk%20inceleme/axkfguqt3v0rrtgkngzb.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Kategorik%20Degiskenler/ilk%20inceleme/yssnv9zcrtgsvimzuiuj.png"
      ]
    }]
    },
{
      "title" : "Numerik Değişken Analizi",
      "results": [
         {
      "title": "Numerik Değişkenler",
      "description": "Numerik Değişkenler resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/il3qnutrmliswxomdh2e.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/rl1on82qbfiv5j6zet2j.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/r1nebjjzhekbzb24ebvm.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/bal37rqkyxpk6rklozvn.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/xzb0dpuftccb9lkycphp.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/l4zf3qu0wtnfoi2wvgh1.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/sge1nhukblvq0eowctro.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/jjjltbocqcgbh3f9qusz.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/gcajaqvkuyo9dgmmp6tf.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100963/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/chdhbkkvs8mkypyyobk9.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100963/analysis/grafikler/Numerik%20Degiskenler/ilk%20inceleme/nt0ka3nmmpjo7wvolmwx.png"
      ]
    }
        ]
    },
    {
      "title" : "Hedef Değişken Analizi",
      "results":[
        { "title": "Day",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan gün paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/day/umoyto45rjdm0ruc7rjt.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/day/wnjetn3rzcdzaqylq5ff.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/day/ypffq37le173cnbl0bme.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/day/vmxqggghivara7w7qemn.png"
      ]},
        {
      "title": "Dept",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan departman paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/dept/fwtvm7fui1kbaleljkph.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/dept/ilw2izqbwrg2vcbghmnh.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/dept/xwrbud5q56m5kxhqdjnc.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/dept/uy2t1gpbmon5nidwguad.png"
      ]
    },

     {
      "title": "isHoliday",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan tatil paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/isholiday/un3dms2b9riyoozlgrja.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/isholiday/nnl7cfnwfrkpculqlmio.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/isholiday/bjohnltfvpt0a7d4ehgx.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/isholiday/blopkfb95yucxvn8t6nn.png"
      ]
    },
    {
      "title": "Month",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan ay paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/month/zrdr3aazwabovwmocv2t.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/month/hrjzvczitissxac9heoc.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/month/s4o1oytrnj6kiyyunff9.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/month/tcn05ycyhhpdks01hmmt.png"
      ]
    },
    {
      "title": "Store",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan mağaza paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/store/zyfxxnliemgb4rqlubfm.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/store/rxu7uc7hhkm1spl5ufoy.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/store/cqybqp8kwuvcyvzcylol.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100972/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/store/zmthqy7drm0zy9bcwnhz.png"
      ]
    },
    {
      "title": "Type",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan tip paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/type/phfcnl7jx7rtwjtp4vbg.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/type/b9fdks33vw43decirbqe.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/type/k9ixhrrmhqkekswubcum.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100970/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/type/yzt6o8i3abawqmjno0j9.png"
      ]
    },
    {
      "title": "Year",
      "description": "Hedef değişken analizi sonrasında kategorik değişkenler içerisinde bulunan yıl paremetresi baz alınarak oluşturulan grafikler aşağıda resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/year/mk5vervxdcbmknuskvxg.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/year/pda1dmploadbvl2nhefi.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/year/hgykhpwezti29tx3iaqh.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100971/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/year/fxgmof0xg57jkm864cxt.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Kategorik%20Degiskenler/oqepsvibc2csmit8mj0l.png"
      ]
    },
    {
      "title": "Numeric",
      "description": "Hedef değişken analizi sonrasında numerik değişkenler resmi ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100969/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/toimfqs6aqwwvm5zp41i.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/jh2h2ndqxssb5qpi55lj.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/oab2vfcynppzan4wif4s.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/wcwohwlfd4qrg3jxnhuh.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/amjdesrrvng43bbtwdut.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/pqljlg1csybj91ijuejx.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/qx19dijueptuzg1ggsj5.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/nsnj2pa60gqfm9vu6gg6.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/zokkdd0kecoz5rb0v7aj.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100968/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/fxeyn7zk3jffwmkpspss.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/subbq0dbpi2zeiyoxaoi.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/lmzrglqemjxl6frajqz1.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/feudfc7qdjj8uhbnjz7s.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/jinaclda7cvpsqecxzr8.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/mof4ajlya1dfxepleb4d.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/csyqdfdivuwhg3xfikcf.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/Hedef%20Degisken%20Analizi/Numerik%20Degiskenler/zrqzjhaed6tehdx7uxsw.png"
      ]
    }

        ]
    },
    {
      "title" : "Korelasyon Analizi",
      "results" :[ {
      "title": "Korelasyon",
      "description": "Eksik Değer resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/Korelasyon%20analizi/x2pxlvudq9on24yqmftw.png"
      ]
    }]
    },
    {
      "title" : "Aykırı Değer Analizi",
      "results" : [
        {
      "title": "Weekly Sales",
      "description": "Outlier Analizi haftalık satışlar resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/1%20weeklysales/cq6amuahgluyjj80mjct.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/1%20weeklysales/jjekqxyldlwnb9m6ohoo.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/1%20weeklysales/nhmvnrwoovm5ay65btho.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/1%20weeklysales/kk3o2zi1uj6iqgd4gxkf.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100965/analysis/grafikler/outlier%20analizi/1%20weeklysales/ptq9fdkirtzhxwsdeq8q.png"
      ]
    },
{
      "title": "Markdown",
      "description": "Outlier Analizi indirimlerinin resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100967/analysis/grafikler/outlier%20analizi/markdowns/sitrossrwvfq4j9ydeqr.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/markdowns/oish0hphobkngbtjamif.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/markdowns/rscbma2yahorddrni2nx.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/markdowns/fvct86pzy0ifisbf33kj.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100966/analysis/grafikler/outlier%20analizi/markdowns/qrljxruh1ulwqy4rwn8u.png"
      ]
    }
        ]
    },
    {
      "title" : "Eksik Değer Analizi",
      "results" :[ {
      "title": "Eksik Değer",
      "description": "Eksik Değer resimleri ile gösterilmiştir.",
      "images": [
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100964/analysis/grafikler/missing%20value/zmvlgxpolb3ykyew8vxu.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100963/analysis/grafikler/missing%20value/dfhg1y9o9yi1kprhfhmj.png",
        "https://res.cloudinary.com/douhpv6i7/image/upload/v1717100963/analysis/grafikler/missing%20value/x1jy19o6wuchwe9xq95o.png"
      ]
    }]
    }
   ]
}

@app.route('/api/getData', methods=['GET'])
def getData():
    return jsonify(data)

if __name__ == '__main__':
    app.run()

