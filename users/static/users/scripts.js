// Start with first post
let counter = 1;

// Load posts 20 at a time
const quantity = 20;

// When DOM loads, render the first 20 posts
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of posts
function load() {

    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add posts
    fetch(`http://127.0.0.1:8000/app/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(add_post);
    })
};
//  <div id="container">
//  <button onclick="myFunction()">Click me!</button>
//   {% for item in items %}
//   <div><a href="{% url 'apps:item' item.id %}"> Item {{ item.id }}</a> Titlle: <b>{{ item.title }}</b> </div>
//   {% endfor %}
  
// </div> 
// Add a new post with given contents to DOM
function add_post(contents) {

    // Create new post
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `<a href="{% url 'apps:item' ${parseInt(contents)} %}" > Item ${contents} </a>`;

    // Add post to DOM
    document.querySelector('#container').append(post);
};