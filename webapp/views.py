from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movies
from .forms import SearchMovie
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from functools import lru_cache
from django.db.models import Q
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer


# Create your views here.


#index.html
def home(request):
    data = Movies.objects.all()
    return render(request, 'webapp/index.html', {'data': data})


@lru_cache
def search(request):
    last_result = search.last_result if hasattr(search, 'last_result') else None
    query = request.GET.get('query', '')
    items = Movies.objects.all()
    items_title = list(items.values_list('original_title','cast'))
    combined_titles=[]
    for i in items_title:
        combined_titles.append(i[0]+' '+i[1])

    print(combined_titles)
    

    vectorizer = TfidfVectorizer()
    #combined_titles = [' '.join(t) for t in items_title]
    combine = vectorizer.fit_transform([query]+combined_titles)
    query_vector = combine[0]
    feature_vectors = combine[1:]
    
    
    results = []
    movies_ = []


    scores = cosine_similarity(combine)
    scores = scores[0]
    print(scores.shape)
    for score, name in zip(scores[1:], items_title):
        if score > 0.2:
            movies_.append((name, score))

    
    for i in movies_:
        matches = Movies.objects.filter(Q(original_title__in = i[0])| Q(cast__in = i[0]))
        results.extend(matches)

    #print(results)

    search.last_result = results

    
    return render(request, 'webapp/search.html', {'last_result': last_result, 'results' : results })

def base(request):
    return render(request, 'webapp/base.html')