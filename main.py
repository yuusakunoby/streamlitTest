from email.mime import base
import os
from tempfile import tempdir
import streamlit as st
import shutil
import  PyPDF2
import base64

def split(filename, outpath ,selected_item):
  reader = PyPDF2.PdfFileReader(filename)
  page_n = reader.getNumPages()
  for page in range(page_n):
    split_page = PyPDF2.PdfFileWriter()
    split_page.addPage(reader.getPage(page))
    savepath = outpath + str(page) + '.pdf'
    with open(savepath, 'wb') as f:
      split_page.write(f)
    if selected_item == 'pdf':
      with open(savepath,'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
      href = f'<a href="data:application/octet-stream;base64,{b64}" download="str(page) + .pdf">download:{page}.pdf</a>'   
      st.markdown(href, unsafe_allow_html=True)
    if selected_item =='zip':
      shutil.make_archive(zipname,'zip', outpath)
      with open('tmp_zip'+'.zip', 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="pdf-controller.zip">download:zip</a>'    
        st.markdown(href, unsafe_allow_html=True)

def file_mk_rm(dirname, zipname):
  if os.path.exists(dirname):
    shutil.rmtree(dirname)
  os.makedirs(dirname, exist_ok=True)
  if os.path.exists(zipname):
    os.remove(zipname)

def page1(tmpdir, zipname):
  st.subheader('Sprit mode')
  input = st.file_uploader("",type='pdf')
  selected_item = st.radio('In what format will save file?',['pdf', 'zip'])
  try:
    if st.button('Run'):
      with st.beta_expander('Download link'):
        file_mk_rm(tempdir,zipname)
        split(input, tmpdir, selected_item, zipname)

  except AttributeError:
    st.error('The file is not select')
    pass      



