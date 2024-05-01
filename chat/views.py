from django.shortcuts import render

def main(request):
    return render(request,'index.html')


def room(request):
    return render(request,'chatroom.html',{
        'room_name':room_name
    })