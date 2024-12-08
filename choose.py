import os

print("Escolha qual ação deseja realizar:")
print("V para baixar video")
print("P para baixar playlist")

escolha = input().lower()
while escolha != "V" and escolha != "v" and escolha != "P" and escolha != "p":
    print("Opção inválida")
    print("Escolha qual ação deseja realizar:")
    print("V para baixar video")
    print("P para baixar playlist")
    escolha = input().lower()

print("Carregando...")

if escolha == "v":
    os.system("python3 ./video_download.py")
elif escolha == "p":
    os.system("python3 ./playlist_download.py")

print("Obrigado por usar o programa!")
