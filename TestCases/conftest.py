import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def Setup(browser):
    if browser=='Chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='Edge':
        driver=webdriver.Edge()
    else:
        opt=webdriver.ChromeOptions()
        opt.add_argument('headless')
        driver=webdriver.Chrome(options=opt)
    driver.maximize_window()
    return driver


@pytest.fixture(params=[
    ("svgade2122@gmail.com","sushant","Pass"),
    ("svgade21222@gmail.com","sushant","Fail"),
    ("svgade2122@gmail.com","sushant12","Fail"),
    ("svgade211222@gmail.com","sushant21","Fail")
])
def getDataForLgoIn(request):
    return request.param


# Select Date From Table:-
# import cx_Oracle
# cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_10")
# con=cx_Oracle.connect('system/sushant@locahost')
# print("connected")
# cur = con.cursor()
# # s1='select * from Students'
# # cur.execute('select * from EMPLOYEES')
# for i in cur:
#     print(i[0],"  ",i[1],"  ",i[2],"  ",i[3],"  ",i[4],"  ",i[5])
# cur.close()
# # con.commit()
# con.close()




