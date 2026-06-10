from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahasiswa
from .forms import MahasiswaForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {
        'mahasiswas': mahasiswas
    })


@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('daftar_mahasiswa')

    else:
        form = MahasiswaForm()

    return render(request, 'mahasiswa/form.html', {
        'form': form,
        'judul': 'Tambah Mahasiswa'
    })


@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)

    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mahasiswa)

        if form.is_valid():
            form.save()
            return redirect('daftar_mahasiswa')

    else:
        form = MahasiswaForm(instance=mahasiswa)

    return render(request, 'mahasiswa/form.html', {
        'form': form,
        'judul': 'Edit Mahasiswa'
    })


@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)

    mahasiswa.delete()

    return redirect('daftar_mahasiswa')


def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)