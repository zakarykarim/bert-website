import streamlit as st
import requests


'''
# Deepfake text detection 💡

## Generated by AI or human-written ?🤔

'''



def get_results(model_name, input_text):
    base_url = 'https://deepfake-ugp33vl5fa-ew.a.run.app/predict'

    params = {
        'model': model_name,
        'X': input_text
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        return st.write("Invalid request")

    result = response.json()

    return result


st.markdown('<link rel="stylesheet" href="custom.css">', unsafe_allow_html=True)

def get_three_results(text):


    dl_cnn = get_results('CNN',text)
    dl_lstm = get_results('LSTM', text)
    dl_gru = get_results('GRU', text)

    return dl_cnn, dl_lstm , dl_gru


url = 'https://deepfake-ugp33vl5fa-ew.a.run.app/predict'

st.session_state['button1'] = True
st.session_state['button2'] = True

firstcol1, firstcol2 = st.columns(2)
st.write('lol2')

with firstcol1:

    text1 = st.text_input('Text 1',
                          value = "Over the past decade, rugby has seen substantial growth both on and off the field, with an increasing number of players participating worldwide. This expansion has sparked a rising interest in the science of rugby, particularly in relation to players' physical preparation. The annual count of rugby-related publications in the fields of sports science and sports medicine has seen a significant rise in recent years.From 2004 to 2023, PubMed featured nearly 4,000 studies using 'rugby' as a keyword. Out of these, approximately 44% (around 1,700 studies) focused on injuries, while only 11% pertained to physical fitness. Examining 'rugby sevens' during the same period, we found 330 studies available. Among these, 35% (approximately 115 studies) concentrated on injury-related aspects, with around 12% (roughly 40 studies) exploring fitness-related topics. It's important to note that the majority of rugby sevens studies emerged after 2009, coinciding with the inclusion of this format in the summer Olympic Games, starting with Rio 2016. Clearly, there exists a pressing demand for further high-quality research in the domain of rugby, particularly concerning physical fitness, training techniques, and conditioning.")
    st.write(f"<p style='text-align: justify;'><i>Text 1: {text1}</i></p>", unsafe_allow_html=True)



with firstcol2:

    text2 = st.text_input('Text 2',
                                        value = "In the last 10 years, rugby has grown on and off the pitch, with an increasing number of players all over the world. These developments have been accompanied by increasing interest in the science of rugby as related to the physical preparation of players. The annual number of rugby publications in the sport-science and sports-medicine literature has increased substantially in recent years. In the period 2004–2023 there were almost 4000 studies in PubMed with “rugby” as a keyword, of which 1700 (∼44%) were injury-focused, but only 11% with “fitness.” In the same period “rugby sevens” returned 330 studies comprising 115 in injury (∼35%) and 40 in fitness (∼12%). The majority of the rugby sevens studies have been published since 2009, when this format of the game was included in the summer Olympic Games (from Rio 2016). Clearly, we need more high-quality rugby research in the areas of physical fitness, training, and conditioning.")
    st.write(f"<p style='text-align: justify;'><i>Text 2: {text2}</i></p>", unsafe_allow_html=True)





secondcol1, secondcol2 = st.columns(2)


with secondcol1:

    if st.button("Predict text 1"):
        #ml_multi1, dl_cnn1, dl_lstm1, dl_gru1, dl_bert1 = get_results(text1)
        #st.write(f"Multinomial : {ml_multi1}%")
        #st.write(f"CNN : {dl_cnn1}%")
        #st.write(f"Multinomial : {dl_lstm1}%")
        #st.write(f"Multinomial : {dl_gru1}%")
        #st.write(f"Multinomial : {dl_bert1}%")
        # Créez trois colonnes de largeur égale
        st.session_state['button1'] = True
        st.session_state['CNN_pred_1'] = list(get_results('CNN',text1).items())
        st.session_state['LSTM_pred_1'] =list( get_results('LSTM',text1).items())
        st.session_state['gru_pred_1'] = list(get_results('GRU',text1).items())

        # CNN_key_1 =
        # LSTM_key_1 =
        # GRU_key_1 =
        #st.session_state['test'] = 'hasnt changed'

with secondcol2:

    if st.button("Predict text 2"):

        # dl_cnn1, dl_lstm1, dl_gru1 = get_results(text1)

        st.session_state['button2'] = True
        st.session_state['CNN_pred_2'] = list(get_results('CNN',text2).items())
        st.session_state['LSTM_pred_2'] = list(get_results('LSTM',text2).items())
        st.session_state['gru_pred_2'] = list(get_results('GRU',text2).items())

        # CNN_key_1 =
        # LSTM_key_1 =
        # GRU_key_1 =


thirdcol1, thirdcol2 = st.columns(2)

with thirdcol1:

    if st.session_state['button1'] == True:



        subcol1, subcol2, subcol3 = st.columns(3)
        # Utilisez Markdown pour centrer les titres
        with subcol1:

            if 'CNN_pred_1' in st.session_state:

                st.markdown("<h2 style='text-align:center;'>CNN</h2>", unsafe_allow_html=True)
                st.image("https://i.postimg.cc/4N0vWLPf/CNN.jpg", caption=f"{st.session_state['CNN_pred_1'][0][0]} ({round(st.session_state['CNN_pred_1'][0][1],2)*100}%)")


        with subcol2:

            if 'LSTM_pred_1' in st.session_state:

                st.markdown("<h2 style='text-align:center;'>LSTM</h2>", unsafe_allow_html=True)
                st.image("https://i.postimg.cc/VLvQjpSK/59908721-escargot-fun.jpg", caption=f"{st.session_state['LSTM_pred_1'][0][0]} ({round(st.session_state['LSTM_pred_1'][0][1],2)*100}%)")

        with subcol3:

            if 'gru_pred_1' in st.session_state:

                st.markdown("<h2 style='text-align:center;'>GRU</h2>", unsafe_allow_html=True)
                st.image("https://i.postimg.cc/d08zsKXV/jesappellegrut.png", caption=f"{st.session_state['gru_pred_1'][0][0]} ({round(st.session_state['gru_pred_1'][0][1],2)*100}%)")

        # dl_cnn2, dl_lstm2, dl_gru2 = get_results(text1)


with thirdcol2:
    if st.session_state['button2'] == True:
        subcol4, subcol5, subcol6 = st.columns(3)
        with subcol4:

            if 'CNN_pred_2' in st.session_state:

                st.markdown("<h2 style='text-align:center;'>CNN</h2>", unsafe_allow_html=True)
                st.image("https://i.postimg.cc/4N0vWLPf/CNN.jpg", caption=f"{st.session_state['CNN_pred_2'][0][0]} ({round(st.session_state['CNN_pred_2'][0][1],2)*100}%)")

        with subcol5:

            if 'LSTM_pred_2' in st.session_state:

                st.markdown("<h2 style='text-align:center;'>LSTM</h2>", unsafe_allow_html=True)
                st.image("https://i.postimg.cc/VLvQjpSK/59908721-escargot-fun.jpg", caption=f"{st.session_state['LSTM_pred_2'][0][0]} ({round(st.session_state['LSTM_pred_2'][0][1],2)*100}%)")

        with subcol6:

            if 'gru_pred_2' in st.session_state:

                st.markdown("<h2 style='text-align:center;'>GRU</h2>", unsafe_allow_html=True)
                st.image("https://i.postimg.cc/d08zsKXV/jesappellegrut.png", caption=f"{st.session_state['gru_pred_2'][0][0]} ({round(st.session_state['gru_pred_2'][0][1],2)*100}%)")
