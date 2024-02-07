# Template generated using ChatGPT
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.uploadedfile import TemporaryUploadedFile
import fitz

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print('File uploaded')
        # Check if a file was uploaded
        if uploaded_file is not None and isinstance(uploaded_file, TemporaryUploadedFile):
            # Open the uploaded file with fitz
            doc = fitz.open(uploaded_file.file)
            print('Files opened')
            # Process the file
            for page in doc:
                for xref in page.get_contents():
                    stream = doc.xref_stream(xref).replace(b'Only for gharishkumar1998@gmail.com', b'')
                    doc.update_stream(xref, stream)
            # Save the PDF to a bytes object
            pdf_bytes = doc.write()
            # Close the document
            doc.close()
            # Create an HTTP response with the PDF content
            response = HttpResponse(pdf_bytes, content_type='application/pdf') 
            response['Content-Disposition'] = 'attachment; filename="redacted.pdf"'
            print('Processed file being send...☺️')
            return response
    return render(request, 'upload.html')

def redact(doc):
    return doc
