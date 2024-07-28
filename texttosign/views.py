from django.shortcuts import render
from .utils import load_folder_content, generate_prompt, get_rephrased_text, convert_to_sign_words

def index(request):
	text = request.GET.get('q')
	if not text:
		return render(request, 'texttosign/index.html')
	folder_content = load_folder_content("D:\\Projects\\signtalkapp\\main\\signtext\\static\\gifs")
	prompt = generate_prompt(text, folder_content)
	rephrased_text = get_rephrased_text(prompt)
	sign_words = convert_to_sign_words(rephrased_text, folder_content)

	context = {"words": sign_words} if sign_words else {}
	return render(request, 'texttosign/index.html', context=context)