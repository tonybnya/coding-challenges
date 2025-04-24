from challenges.models import Challenge

for challenge in Challenge.objects.all():
    if challenge.icon.startswith('/static/challenges/'):
        # Already has the correct path
        continue
    elif challenge.icon.startswith('/static/'):
        # Has /static/ prefix but not in the right place
        icon_file = challenge.icon.split('/')[-1]
        challenge.icon = f'/static/challenges/{icon_file}'
    else:
        # Doesn't have /static/ prefix
        icon_file = challenge.icon.split('/')[-1]
        challenge.icon = f'/static/challenges/{icon_file}'
    challenge.save()

print("Updated icon paths:")
for challenge in Challenge.objects.all():
    print(f"{challenge.id}: {challenge.title} - {challenge.icon}")
