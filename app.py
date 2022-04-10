from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)

original_questions = {
 #Format is 'question':[options]
 'what is your current BMI i.e. weight/height^2?':['less than 18.5','18.5 to 24.9','25 to 29.9','30 or more'],
 'Average work time?':['8 hours','10 hours','12 hours','more than 12 hours'],
 'Do you have dibetes?':['yes','no'],
 'Do you have High Blood Pressure?':['yes','no'],
 'Do you have a problem of muscle ache?':['yes','no'],
 'Do you feel left out or have FOMO sometimes?':['yes','no'],
 'Do you get time to spend with your friends and family?':['yes','no']
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
 """
 This function is for shuffling
 the dictionary elements.
 """
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(q.keys())
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

@app.route('/')
def quiz():
 questions_shuffled = questions
 for i in questions.keys():
  random.shuffle(questions[i])
 return render_template('index.html', q = questions_shuffled, o = questions)
 
@app.route('/quiz', methods=['POST'])
def quiz_answers():
 output=""
 if request.form['what is your current BMI i.e. weight/height^2?'].equals('less than 18.5'):
    output1=output+"You are underweight please consult a dietitian. "
 if request.form['what is your current BMI i.e. weight/height^2?'].equals('18.5 to 24.9'):
    output1=output+"Your weight is in the correct range. "
 if request.form['what is your current BMI i.e. weight/height^2?'].equals('25 to 29.9'):
    output1=output+"You are a little overweight please add 30 minutes of physical activity in your schedule. "
 if request.form['what is your current BMI i.e. weight/height^2?'].equals('30 or more'):
    output1=output+"Your weight is in the obese range please consult a professional and add atleast 1 hour of physical activity in your routine. "
 if request.form['Average work time?'].equals('8 hours'):
    output2=output1+"Your work hours are sufficient and in the right range. "
 if request.form['Average work time?'].equals('10 hours'):
    output2=output1+"Your work hours are slightly more than required work timings. "
 if request.form['Average work time?'].equals('12 hours'):
    output2=output1+"Your work hours are more than what is required, please try to avoid working late to avoid burnout. "
 if request.form['Average work time?'].equals('more than 12 hours'):
    output2=output1+"You are prone to burnout, please consult your supervisor and get the workload distributed to other team members. "
 if request.form[ 'Do you have High Blood Pressure?'].equals('yes'):
    output3=output2+"Please avoid stressful situations and overwork. "
 if request.form[ 'Do you have High Blood Pressure?'].equals('no'):
    output3=output2+""
 if request.form['Do you have a problem of muscle ache?'].equals('yes'):
    output4=output3+"Please improve your body posture and try to add half an hour of yoga in your schedule. "
 if request.form['Do you have a problem of muscle ache?'].equals('no'):
    output4=output3+""
 if request.form['Do you feel left out or have FOMO sometimes?'].equals('yes'):
    output5=output4+"Try adding 1 or 2 hours of family and friends time in your schedule. "
 if request.form['Do you feel left out or have FOMO sometimes?'].equals('no'):
    output5=output4+""
 else:
    output5="no recommendations"
 return '<h1>Recommendations: <u>'+output5+'</u></h1>'

if __name__ == '__main__':
 app.run(debug=True)
