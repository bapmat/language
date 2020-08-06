
# 파이썬으로 두 개의 엑셀 파일을 비교하기: excel diff (https://hogni.tistory.com/89)
# 컬림 : 아이디 / 브랜드 / 상품명 / 정가 / 판매가
# 두 파일을 비교하기 위해서는, 두 파일 모두 동일한 컬럼 순서를 가지고 있고 개별 행 데이터를 구분할 수 있는 고유한 값을 지닌 컬럼이 존재해야 합니다. 
# 예제 코드에서는 '아이디' 컬럼을 활용하겠습니다.

# ********************** 삭제된 데이터와 새로 추가된 데이터를 찾아내기 **********************
# pandas 라이브러리를 불러옵니다.
import pandas as pd

# 비교할 엑셀 파일들을 불러옵니다. 
df_old = pd.read_excel('data_old.xlsx')
df_new = pd.read_excel('data_new.xlsx')

# 어떤 파일이 예전에 만들어진 파일이고 어떤 파일이 새로운 파일인지 구분하기 위해 컬럼을 추가합니다.
df_old['ver'] = 'old'
df_new['ver'] = 'new'

# set 함수를 이용하면 손쉽게 새로 추가된 데이터와 이전에 있었지만 삭제된 데이터를 발라낼 수 있습니다.
id_dropped = set(df_old['아이디']) - set(df_new['아이디'])
id_added = set(df_new['아이디']) - set(df_old['아이디'])

print('삭제된 아이템: ',id_dropped)
print('추가된 아이템: ',id_added)
 

df_dropped = df_old[df_old['아이디'].isin(id_dropped)].iloc[:,:-1]
df_added = df_new[df_new['아이디'].isin(id_added)].iloc[:,:-1]


# ********************** 내용이 변경된 데이터 찾기 **********************
# 두 데이터프레임을 하나로 합칩니다.
df_concatted = pd.concat([df_old, df_new], ignore_index=True)
# 모든 컬럼의 내용이 중복되는 데이터는 삭제합니다.
changes = df_concatted.drop_duplicates(df_concatted.columns[:-1], keep='last')

# 남은 데이터 중 동일한 아이디 값이 두개 이상 존재한다면
# 정보가 변경된 데이터입니다.
duplicated_list = changes[changes['아이디'].duplicated()]['아이디'].to_list()
df_changed = changes[changes['아이디'].isin(duplicated_list)]


# 이렇게 처리된 데이터프레임은 위의 사진처럼 이전 데이터와 새롭게 업데이트된 데이터가 모두 들어있습니다.
# 다시 두 개의 데이터프레임으로 분리하겠습니다.
df_changed_old = df_changed[df_changed['ver'] == 'old'].iloc[:,:-1]
df_changed_old.sort_values(by='아이디', inplace=True)

df_changed_new = df_changed[df_changed['ver'] == 'new'].iloc[:,:-1]
df_changed_new.sort_values(by='아이디', inplace=True)


# 반복문으로 두 데이터프레임 내 값을 차례대로 비교해서 그 결과를 정리
df_info_changed = df_changed_old.copy()
for i in range(len(df_changed_new.index)):
    for j in range(len(df_changed_new.columns)):
        if (df_changed_new.iloc[i, j] != df_changed_old.iloc[i, j]):
            df_info_changed.iloc[i,j] = str(df_changed_old.iloc[i, j]) + " ==> " + str(df_changed_new.iloc[i,j])


# ********************** 비교 결과를 엑셀로 저장하기 **********************
# 두 파일을 비교한 결과를 엑셀로 저장하겠습니다.
# 이 파일은 세 개의 시트로 구성됩니다. ->  ①내용이 변경된 데이터, ②새롭게 추가된 데이터, ③기존에 있다가 삭제된 데이터
with pd.ExcelWriter('compared_result.xlsx') as writer:
    df_info_changed.to_excel(writer, sheet_name='info changed', index=False)
    df_added.to_excel(writer, sheet_name='added', index=False)
    df_dropped.to_excel(writer, sheet_name='dropped', index=False)    




'''
def compare_excel(old_xlsx, new_xlsx, column_name):
    import pandas as pd    
    df_old = pd.read_excel(old_xlsx)
    df_new = pd.read_excel(new_xlsx)

    # 불러온 데이터의 버전 구분
    df_old['ver'] = 'old'
    df_new['ver'] = 'new'

    id_dropped = set(df_old[column_name]) - set(df_new[column_name])
    id_added = set(df_new[column_name]) - set(df_old[column_name])

    # 삭제된 데이터
    df_dropped = df_old[df_old[column_name].isin(id_dropped)].iloc[:,:-1]

    # 추가된 데이터
    df_added = df_new[df_new[column_name].isin(id_added)].iloc[:,:-1]

    df_concatted = pd.concat([df_old, df_new], ignore_index=True)
    changes = df_concatted.drop_duplicates(df_concatted.columns[:-1], keep='last')
    duplicated_list = changes[changes[column_name].duplicated()][column_name].to_list()
    df_changed = changes[changes[column_name].isin(duplicated_list)]

    df_changed_old = df_changed[df_changed['ver'] == 'old'].iloc[:,:-1]
    df_changed_old.sort_values(by=column_name, inplace=True)

    df_changed_new = df_changed[df_changed['ver'] == 'new'].iloc[:,:-1]
    df_changed_new.sort_values(by=column_name, inplace=True)

    # 정보가 변경된 데이터 정리
    df_info_changed = df_changed_old.copy()
    for i in range(len(df_changed_new.index)):
        for j in range(len(df_changed_new.columns)):
            if (df_changed_new.iloc[i, j] != df_changed_old.iloc[i, j]):
                df_info_changed.iloc[i,j] = str(df_changed_old.iloc[i, j]) + " ==> " + str(df_changed_new.iloc[i,j])

    # 엑셀 저장            
    with pd.ExcelWriter('compared_result.xlsx') as writer:
        df_info_changed.to_excel(writer, sheet_name='info changed', index=False)
        df_added.to_excel(writer, sheet_name='added', index=False)
        df_dropped.to_excel(writer, sheet_name='dropped', index=False)
'''