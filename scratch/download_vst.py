import urllib.request
from PIL import Image

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

vst_url = "https://upload.wikimedia.org/wikipedia/commons/9/93/VST_Mitsubishi_VT224-1D_Tractor_Front_Kulisholai_Sep25_A7CR_07587.jpg"

try:
    req = urllib.request.Request(vst_url, headers=headers)
    with urllib.request.urlopen(req) as resp, open("vst_mini_tractor.jpg", "wb") as f:
        f.write(resp.read())
    im = Image.open("vst_mini_tractor.jpg")
    print("Downloaded vst_mini_tractor:", im.size)
except Exception as e:
    print("Error:", e)
