from flask import Flask,render_template,redirect,url_for,flash,request 
#from flask import Flask, render_template,url_for
from forms import NounForm,VerbForm,OtherForm
import numpy as np
import pandas as pd
import tablib
import os


app=Flask(__name__)
app.config['SECRET_KEY']='e80221527ae2691b4130960d62e5843b'


@app.route("/")
@app.route("/home")
def home():
  return render_template('HOME.html',)
    

dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'lexicon.csv')) as f:dataset.csv = f.read()

@app.route("/VIEW",methods=['GET','POST'])
def VIEW():
  data = dataset.html
  return render_template('VIEW.html',data=data)

@app.route("/Noun",methods=['GET','POST'])
def Noun():
    form=NounForm()
    Genders = ['ಪುರುಷ ', 'ಸ್ತ್ರೀ ', 'ಇತರೆ']
    Noun_categories=['1(ನು - ಹುಡುಗ)','2(ನು - ಅಣ್ಣ)','3(ಳು-ಕಮಲ)','4(ಳು - ಅಕ್ಕ )','5(ವು - ಮರ )','6(ದು - ಚಿಕ್ಕ )','7(ಯು - ಕವಿ )','8(ಯು - ಗೌರಿ )',
                     '9(ಯು - ತಾಯಿ )','10(ವು - ಗುರು )','11(ಉ - ಹೆಣ್ಣು )','12(ಯು - ತಂದೆ )']
#    if form.validate_on_submit():
#         if 'ಮುಖಪುಟ' in request.form:return redirect(url_for('home'))
#    
    if form.is_submitted():
        return redirect(url_for('home'))
    return render_template('NOUN.html',title='Noun',form=form,Genders=Genders,Noun_categories=Noun_categories)


@app.route("/Verb",methods=['GET','POST'])
def Verb():
    form=VerbForm()
    Present_tense=['1R (ತ್ತಾನೆ - ತಿನ್ನು )','2R (ಯುತ್ತಾನೆ - ಕುಡಿ )',]
    Future_tense=['1F (ವನು - ಕಾಡು )','2F (ಯುವನು = ಹರಿ )']
    Past_tense=['1S (ಅಂದನು -ತಿನ್ನು )','2S (ಅಂಡನು -ಕಾಣು )','3S (ಕ್ಕನು - ನಗು )','4S (ತ್ತನು - ಅಳು )','5S  (ಟ್ಟನು - ಈಡು)','6S (ದ್ದನು - ಬೀಳು )','7S (ಇದನು - ಹಾಡು )','8S (ಗ್ಗಿದನು - ಬಾಗು )','9S (ದನು - ಬರೆ)','10S (ಅಂತನು- ನಿಲ್ಲು )']
#    if form.validate_on_submit():
#         if 'ಮುಖಪುಟ' in request.form:return redirect(url_for('home'))
#    
    if form.is_submitted():
        return redirect(url_for('home'))
    return render_template('VERB.html',title='Verb',form=form,Present_tense=Present_tense,Future_tense=Future_tense,Past_tense=Past_tense)

@app.route("/Other",methods=['GET','POST'])
def Other():
    form=OtherForm()
    Other_categories=['ವಿಶೇಷಣ','ಕ್ರಿಯಾವಿಶೇಷಣ','ಅವ್ಯಯ']
#    if form.validate_on_submit():
#         if 'ಮುಖಪುಟ' in request.form:return redirect(url_for('home'))
#    
    if form.is_submitted():
        return redirect(url_for('home'))
    return render_template('OTHER.html',title='Other',form=form,Other_categories=Other_categories)
    

@app.route("/result1", methods= ['GET','POST'])
def result1():
   output1 = request.form['Noun_word']
   output2='N'
   output3 = request.form['Genders']
   if (output3 == 'ಪುರುಷ' ):output3='M'
   if (output3 == 'ಸ್ತ್ರೀ' ):output3='F'
   if (output3 == 'ಇತರೆ' ):output3='X'
   output4 = request.form['Noun_categories']
   
   if (output4 == '1(ನು - ಹುಡುಗ)'):output4='1'
   if (output4 == '2(ನು - ಅಣ್ಣ)'):output4='2'
   if (output4 == '3(ಳು-ಕಮಲ)'):output4='3'
   if (output4 == '4(ಳು - ಅಕ್ಕ )'):output4='4'
   if (output4 == '5(ವು - ಮರ )'):output4='5'
   if (output4 == '6(ದು - ಚಿಕ್ಕ )'):output4='6'
   if (output4 == '7(ಯು - ಕವಿ )'):output4='7'
   if (output4 == '8(ಯು - ಗೌರಿ )'):output4='8'
   if (output4 == '9(ಯು - ತಾಯಿ )'):output4='9'
   if (output4 == '10(ವು - ಗುರು )'):output4='10'
   if (output4 == '11(ಉ - ಹೆಣ್ಣು )'):output4='11'
   if (output4 == '12(ಯು - ತಂದೆ )'):output4='12'
   
   
   #final_output=output1 +"\t\t\t"+ output2 +"\t\t" + output3+'\t\t'+output4
   final_output=output1 +","+ output2 +"," + output3+","+output4+","+","
   if output1 != "":save(final_output)
   return redirect(url_for('home'))

@app.route("/result2", methods= ['GET','POST'])
def result2():
   output1 = request.form['Verb_word']
   output2='V'
   output3 = request.form['Present_tense']
   if (output3 == '1R (ತ್ತಾನೆ - ತಿನ್ನು )'):output3='1R'
   if (output3 == '2R (ಯುತ್ತಾನೆ - ಕುಡಿ )'):output3='2R'
   
   output4 = request.form['Future_tense']
   
   if (output4 == '1F (ವನು - ಕಾಡು )'):output4='1F'
   if (output4 == '2F (ಯುವನು = ಹರಿ )'):output4='2F'
   output5 = request.form['Past_tense']
  
   if (output5 == '1S (ಅಂದನು -ತಿನ್ನು )'):output5='1S'
   if (output5 == '2S (ಅಂಡನು -ಕಾಣು )'):output5='2S'
   if (output5 == '3S (ಕ್ಕನು - ನಗು )'):output5='3S'
   if (output5 == '4S (ತ್ತನು - ಅಳು )'):output5='4S'
   if (output5 == '5S  (ಟ್ಟನು - ಈಡು)'):output5='5S'
   if (output5 == '6S (ದ್ದನು - ಬೀಳು )'):output5='6S'
   if (output5 == '7S (ಇದನು - ಹಾಡು )'):output5='7S'
   if (output5 == '8S (ಗ್ಗಿದನು - ಬಾಗು )'):output5='8S'
   if (output5 == '9S (ದನು - ಬರೆ)'):output5='9S'
   if (output5 == '10S (ಅಂತನು- ನಿಲ್ಲು )'):output5='10S'
   
   
    # final_output=output1 +"\t\t\t"+ output2 +"\t\t" + output3 +"\t\t"+ output4 +"\t\t" + output5
   
   final_output=output1 +","+ output2 +"," +" "+","+ output3 +","+ output4 +"," + output5

   if output1 != "":save(final_output)
   return redirect(url_for('home'))

@app.route("/result3", methods= ['GET','POST'])
def result3():
   output1 = request.form['Other_word']
   output2 = request.form['Other_categories']
   #final_output=output1 +"\t\t\t"+ output2 
   if(output2 == 'ವಿಶೇಷಣ'):output2='J'
   if(output2 == 'ಕ್ರಿಯಾವಿಶೇಷಣ'):output2='D'
   if(output2 == 'ಅವ್ಯಯ'):output2='A'
   
   final_output=output1 +","+ output2+","+","+","+","
   
   if output1 != "":save(final_output)
   return redirect(url_for('home'))



def save(text, filepath='lexicon.csv'):
    lexicon_rows=[]
    lexicon = pd.read_csv('lexicon.csv')
    lexicon = lexicon.replace(np.nan,"", regex=True)
    for index, rows in lexicon.iterrows():
        row_stg=str(rows.WORD)+','+str(rows.GRAMMATICAL_CATEGORY)+','+str(rows.GENDER)+','+str(rows.PRESENT_TENSE_CATEGORY)+','+str(rows.FUTURE_TENSE_CATEGORY)+','+str(rows.PAST_TENSE_CATEGORY)
        lexicon_rows.append(row_stg) 
    
    if text not in lexicon_rows:
        with open("lexicon.csv", "a") as f:
            f.write(text)
            f.write('\n')

if __name__=='__main__':
    app.run(debug=True)