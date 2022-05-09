import streamlit as st
import shutil
import PyPDF2
import base64
import tkinter.filedialog

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
def file_select():
  tmpdir = tkinter.filedialog.askdirectory()

def main():
  st.subheader('Sprit mode')
  input = st.file_uploader("",type='pdf')
  selected_item = st.radio('In what format will save file?',['pdf', 'zip'])
  
  try:
    if st.button('RefDir'):
      tmpdir = tkinter.filedialog.askdirectory()

    if st.button('Run'):
      root = tkinter.Tk()
# topmost指定(最前面)
      root.attributes('-topmost', True)
      root.withdraw()
      root.lift()
      root.focus_force()
      tmpdir = tkinter.filedialog.askdirectory(parent=root)
      with st.expander('Download link'):
        split(input, tmpdir, selected_item)

  except AttributeError:
    st.error('The file is not select')
    pass      

if __name__ == "__main__":
  main()


