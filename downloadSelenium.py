from selenium import webdriver

options = webdriver.ChromeOptions()

chrome_path = r"C:\Users\lucas.zarza\Desktop\Code\chromedriver.exe"

#driver = webdriver.Chrome(chrome_path, chrome_options=options)#.(options=option) -> Faz rodar em background

#------
prefs = {"download.default_directory" : 'C:\\Users\\lucas.zarza\\Desktop\\webscraping\\melhorias\\download_files_bbce\\'}
options.add_experimental_option("prefs", prefs)
options = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)
#--------
options.get("https://www.whatsapp.com/download")
options.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/a").click()

#"download.default_directory","C:\\Users\\xxx\\downloads\\Test"


