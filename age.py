driving = input("你有開過車嗎？")
age = input("你的年齡是？")
age = int(age)

if driving == "有":
	if age >= 18:
		print("你通過測驗了")
	else:
		print("奇怪，你還沒滿18歲怎會開過車????")
elif driving == "沒有":
	if age >= 18:
		print("那你可以考駕照了!")
	else:
		print("過幾年你就可以考駕照了~~")
else:
	print("只能回答『 有 』或『 沒有 』")
