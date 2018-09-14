from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  #返回结果

from .forms import PdfUpoadForm  # 导入表单

import PyPDF2       # 导入处理包


def pdf_extract(request):
    if request.method == 'POST':
        # 如果用户通过POST提交
        form = PdfUpoadForm(request.POST, request.FILES)

        if form.is_valid():
            # 如果用户表单通过验证，获取提取文件页面码
            page_num = int(request.POST.get('page'))

            # pdf文档页码对象编码是从0开始， 所以减一
            page_index = page_num - 1

            # 获取上传的文件
            f = request.FILES['file']

            # 打开上传的文件
            with open('original.pdf', 'wb+') as pdfFileObj:
                for chunk in f.chunks():
                    pdfFileObj.write(chunk)

                # 利用PyPDF2 读取新的PDF 文件
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                # 提取页面
                pageObj = pdfReader.getPage(page_index)

                # 创建新的PDF文件
                pdfWriter = PyPDF2.PdfFileWriter()

                # 添加已读取的页面对象
                pdfWriter.addPage(pageObj)

                #提取的页面写入新的PDF文件
                with open('extracted_pages.pdf', 'wb') as pdfOutFile:
                   pdfWriter.write(pdfOutFile)

                # 打开新的PDF文件， 输出。
                with open('extracted_pages.pdf', 'rb') as pdfExtract:
                    response = HttpResponse(pdfExtract.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment: filename="extracted_page_{}.pdf"'.format(page_num)
                    return response
        else:
            # 如果用户没有通过POST，提交生成空表单

            form = PdfUpoadForm()

            return render(request, 'PDF/pdf_upload.html', {'form': form})



