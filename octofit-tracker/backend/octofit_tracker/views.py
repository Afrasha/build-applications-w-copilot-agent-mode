from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://obscure-space-train-p7jxp7w759jc6p6w-8000.app.github.dev"
    })