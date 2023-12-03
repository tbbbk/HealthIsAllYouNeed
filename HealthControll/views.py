from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def record(request):
    if request.method == "GET":
        return render(request, 'record.html')
    age = request.POST.get('age')
    weight = request.POST.get('weight')
    height = request.POST.get('height')
    target = request.POST.get('target')
    gender = request.POST.get('sex')
    print(age, weight, height, target, gender)
    return redirect('/index/')

@login_required
def make_fit_plan(request):
    if request.method == 'GET':
        return render(request, "make_fit_plan.html")
    name = request.POST.get('name')
    age = request.POST.get('age')
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    target = int(request.POST.get('target'))
    gender = request.POST.get('gender')
    intensity = int(request.POST.get('intensity'))
    date = request.POST.getlist('exercise_days[]')
    plan = workout_schedule(age=age, gender=gender, weight=weight, height=height, target_weight=target, exercise_intensity=intensity, exercise_days=date)
    # 在视图中对字典进行处理，转换为可以直接在模板中遍历的列表
    plan_list = [{'day': day, 'details': details} for day, details in plan.items()]
    return render(request, "make_fit_plan.html", {'plan_list': plan_list})


@login_required
def make_fit_plan(request):
    if request.method == 'GET':
        return render(request, "make_fit_plan.html")
    name = request.POST.get('name')
    age = request.POST.get('age')
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    target = int(request.POST.get('target'))
    gender = request.POST.get('gender')
    intensity = int(request.POST.get('intensity'))
    date = request.POST.getlist('exercise_days[]')
    plan = workout_schedule(age=age, gender=gender, weight=weight, height=height, target_weight=target, exercise_intensity=intensity, exercise_days=date)
    plan_list = [{'day': day, 'details': details} for day, details in plan.items()]
    return render(request, "make_fit_plan.html", {'plan_list': plan_list})


@login_required
def make_diet_plan(request):
    if request.method == 'GET':
        return render(request, "make_diet_plan.html")
    name = request.POST.get('name')
    age = request.POST.get('age')
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    target = int(request.POST.get('target'))
    gender = request.POST.get('gender')
    taboo = request.POST.get('taboo')
    food = request.POST.getlist('food[]')
    plan = generate_diet_plan(food)
    return render(request, 'make_diet_plan.html', {'plan_list': plan})


@login_required
def make_part_plan(request):
    if request.method == 'GET':
        return render(request, "make_part_plan.html")
    name = request.POST.get('name')
    age = request.POST.get('age')
    weight = int(request.POST.get('weight'))
    height = int(request.POST.get('height'))
    target = int(request.POST.get('target'))
    gender = request.POST.get('gender')
    part = request.POST.getlist('parts[]')
    plan = generate_part_plan(part, abs(weight - target))
    return render(request, 'make_part_plan.html', {'plan_list': plan})


@login_required
def generate_part_plan(parts, diff):
    plan = {'plan': []}
    for part in parts:
        if part == 'foot':
            plan['plan'].append(f'腿部：每天跑步{diff + 30}分钟')
        if part == 'breast':
            plan['plan'].append(f'胸部：每天俯卧撑{diff + 100}个')
        if part == 'abdomen':
            plan['plan'].append(f'腹部：每天仰卧起坐{diff + 150}个')
        if part == 'arm':
            plan['plan'].append(f'手臂：每天引体向上{diff + 50}个')
    return plan


def calculate_bmi(weight, height):
    height_in_meters = height / 100  # 将身高从厘米转换为米
    bmi = weight / (height_in_meters ** 2)
    return bmi


def generate_diet_plan(foods):
    plan = {'breakfast': [], 'lunch': [], 'dinner': []}
    vegetable = ['青菜', '白菜', '绿叶菜']
    noodle = ['一两面条', '二两面条', '一两面条']
    flesh = ['鱼肉', '牛肉', '猪肉']
    for food in foods:
        if food == 'vegetable':
            plan['breakfast'].append(vegetable[0])
            plan['lunch'].append(vegetable[1])
            plan['dinner'].append(vegetable[2])
        if food == 'noodle':
            plan['breakfast'].append(noodle[0])
            plan['lunch'].append(noodle[1])
            plan['dinner'].append(noodle[2])
        if food == 'flesh':
            plan['breakfast'].append(flesh[0])
            plan['lunch'].append(flesh[1])
            plan['dinner'].append(flesh[2])
    return plan



def generate_workout_plan(bmi, target_weight, exercise_intensity, exercise_days, weight):
    # 根据BMI、目标体重、锻炼强度和锻炼日期生成锻炼计划
    # 返回一个字典，包括每天的锻炼类型和时间

    # 根据不同的锻炼强度设置锻炼类型和时间
    if exercise_intensity >= 7:
        exercise_type = '高强度训练'
        exercise_time = 60  # 高强度训练时间为60分钟
    elif exercise_intensity >= 4:
        exercise_type = '中等强度训练'
        exercise_time = 45  # 中等强度训练时间为45分钟
    else:
        exercise_type = '低强度训练'
        exercise_time = 30  # 低强度训练时间为30分钟

    # 根据目标体重和当前体重差异调整锻炼计划
    weight_difference = target_weight - weight
    if weight_difference > 0:
        # 如果目标体重大于当前体重，增加有氧运动时间
        exercise_type = '有氧运动'
        exercise_time += 15  # 增加15分钟有氧运动

    # 根据不同的日期分配锻炼计划
    workout_schedule = {}
    for day in exercise_days:
        workout_schedule[day] = {'exercise_type': exercise_type, 'minute': exercise_time}

    return workout_schedule

def workout_schedule(age, gender, weight, height, target_weight, exercise_intensity, exercise_days):
    bmi = calculate_bmi(weight, height)
    exercise_plan = generate_workout_plan(bmi, target_weight, exercise_intensity, exercise_days, weight)
    return exercise_plan
