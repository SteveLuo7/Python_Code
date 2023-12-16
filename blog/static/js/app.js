document.addEventListener('DOMContentLoaded', function () {
    // Placeholder data for blog posts
    const posts = [
        {
            title: 'First Blog Post',
            date: 'January 1, 2023',
            content: 'This is my first blog post. Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        },
        {
            title: 'Another Post',
            date: 'February 15, 2023',
            content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit dui vel nisi bibendum euismod.'
        }
    ];

    const blogPostsContainer = document.getElementById('blog-posts');

    // Render blog posts
    posts.forEach(post => {
        const postElement = document.createElement('article');
        postElement.innerHTML = `
            <h2>${post.title}</h2>
            <time datetime="${post.date}">${post.date}</time>
            <p>${post.content}</p>
        `;
        blogPostsContainer.appendChild(postElement);
    });
});
