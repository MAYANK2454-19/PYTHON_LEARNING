
has_experience = False
has_degree = False
meets_age = True
reject_application = (not has_experience and not has_degree) or not meets_age

print(reject_application)