import time
time.sleep(.5)
print("Xin chào!")
time.sleep(.5)
print("Tôi là chương trình Python.")
time.sleep(1.2)
print("Rất vui khi được gặp bạn!")
time.sleep(1)
print("Có thể cho tôi biết tên của bạn được không?")
time.sleep(2)
print("Bạn có muốn nhập tên?")
while True:
    nhap = input("Có hoặc Không?: ")
    if nhap == "có":
        print("Xác nhận bạn muốn nhập tên.")
        nhap2 = input("Nhập tên của bạn: ")
        print("Chào bạn", nhap2)
    else:
        print("Xác nhận bạn không muốn nhập tên.")
        print("Vậy tôi sẽ gọi bạn là người dùng.") 
        break