# Muhammad Falihul Abad Arsyil Adzim Karim / 220535603278 / Teknik Informatika B

v = "aiueoAIUEO"
k = input("ketik kata :")
for hur in k:
    if(hur in v):
        k = k.replace(hur, "")
print(k)