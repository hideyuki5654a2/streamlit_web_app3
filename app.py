import streamlit as st
import pandas as pd
from PIL import Image
import datetime
import matplotlib.pyplot as plt

st.title('Streamlit初号機')
st.caption('これはStreamlitのWebアプリ第一号です')

col1,col2=st.columns(2)

with col1:
 
        #テキスト       
        st.subheader('PythonWeb開発')
        st.text('Pythonでスマホアプリを作るプロジェクトです。\n'
                'これが成功したら仕事で使えるスマホアプリを作ってみる')
        code= '''
        import streamlit as st

        st.title('Streamlit初号機')
        '''
        st.code(code,language='python')
        #画像
        image=Image.open('absolutvision-82TpEld0_e4-unsplash.jpg')
        st.image(image,width=350)

        with st.form(key='profile_form'):
                #テクストボックス
                name=st.text_input('名前')
                address=st.text_input('住所')
                
                #セレクトボックス
                age_category=st.radio(
                        '年齢層',
                        ('子ども(18才未満)','大人(18才以上)'))
                
                #複数選択
                hobby=st.multiselect(
                        '趣味',
                        ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理'))
                
                #チェックボックス
                mail_subscribe=st.checkbox('メールマガジンを購読する')
                
                #スライダー
                height=st.slider('身長',min_value=110,max_value=210)
                
                #日付
                start_date=st.date_input(
                        '開始日',
                        datetime.date(2022,8,30))
                
                #カラーピッカー
                color=st.color_picker('テーマカラー','#00f900')

                #ボタン
                submit_btn=st.form_submit_button('送信')
                cancel_btn=st.form_submit_button('キャンセル')
                if submit_btn:
                        st.text(f'ようこそ！{name}さん！{address}に郵送しました！')
                        st.text(f'年齢層:{age_category}')
                        st.text(f'趣味：{",".join(hobby)}')

with col2:
           
        #データ分析関連
        df=pd.read_csv('weather.csv',index_col='年月日',encoding='shift_jis')
        st.dataframe(df)
        #st.table(df)
        st.line_chart(df)
        st.bar_chart(df)

        #matplotlib
        fig,ax=plt.subplots()
        ax.plot(df.index,df)
        ax.set_title('matplotlib graph')
        st.pyplot(fig)