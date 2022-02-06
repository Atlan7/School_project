from formulas.models import Theme, Formula

import random


def querySet_to_list(qs):
     return [i['id'] for i in qs]

    
def randomize_quesions(quantity_questions ,pks_of_avalible_formulas ):
    """ Перемешиваю вопросы и возвращаю словарь {id вопроса: [варианты ответов]} """
#    print(pks_of_avalible_formulas)
    pks_of_avalible_formulas = random.sample(pks_of_avalible_formulas, len(pks_of_avalible_formulas))
#    print(pks_of_avalible_formulas)
    questions = {}
    questions_db = {}
    min_id = Formula.objects.all().first().id 
    max_id = Formula.objects.all().last().id 

    for i in range(quantity_questions):
        answers = [pks_of_avalible_formulas[i]]
        answers_db = []
        answers_db.extend(Formula.objects.filter(pk=pks_of_avalible_formulas[i]))
        question_id = pks_of_avalible_formulas[i] 

        while len(answers) != 4: 
            suggested_pk = random.randint(min_id, max_id)
            if suggested_pk not in answers and suggested_pk != question_id: 
                answers.append(suggested_pk)
                answers_db.extend(Formula.objects.filter(pk=suggested_pk))

        questions_db[Formula.objects.filter(pk=question_id).first()] = random.sample(answers_db, len(answers_db)) 

    return questions_db


def get_questions(request, form):
    context = {'form': form}

    theme_ids = form.cleaned_data['themes'].values_list('id', flat=True)
    quantity_questions = form.cleaned_data['quantity_questions']

    pks_of_avalible_formulas = []

    for i in range(len(theme_ids)):
        formulas = Formula.objects.filter(theme_id=theme_ids[i]).values('id')
        pks_of_avalible_formulas.extend(querySet_to_list(formulas))
    
    if quantity_questions > len(pks_of_avalible_formulas):
        if len(theme_ids) > 1:
            raise ValueError(f"Для данных тем максимальное кол-во вопросов: {len(pks_of_avalible_formulas)}")
        else:
            raise ValueError(f"Для данной темы максимальное кол-во вопросов: {len(pks_of_avalible_formulas)}")
    else: 
#        print(pks_of_avalible_formulas)
        questions = randomize_quesions(quantity_questions, pks_of_avalible_formulas)

        context['questions'] = questions  
#    print(formulas_quantity, all_formulas)

    return context


def results_of_quiz(answers):
    results = []
    total_questions = 0
    total_right_answers = 0

    for i in range(len(answers)):
        right_answer = Formula.objects.get(id=answers[i][0])

        if answers[i][0] == answers[i][1]:
            total_right_answers += 1
            results.append([right_answer, right_answer])
        elif type(answers[i][1]) != str: 
            gotten_answer = Formula.objects.get(id=answers[i][1])
            results.append([right_answer, gotten_answer])
        else:
            results.append([right_answer, 'None'])

        total_questions +=1

    return results, total_right_answers, total_questions


