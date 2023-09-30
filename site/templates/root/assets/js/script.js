const descriptionContainer = document.getElementById("descriptionContainer");
const descriptions = [
    "Hello! My name is Bart, and I'm passionate about data science and programming. \n I'm currently pursuing my studies in Applied Computer Science at University in Katowice.",
    "My Interests:",
    "I have strong interest in data science and machine learning. I want to expand my knowledge in this field and exploring new techniques and technologies.  ", 
    "I have a bit of experience with python and I'm continually expanding my knowledge in this language. \n It's my first language that I tryied to learn.\n And I think it was good decision :) ",
    "In the future, I aspire to work in the field of data science, when I can apply my skills to solve real-world problems and make data-driven decisions. ",
    "GET IN TOUCH",
    "I'm always open to new opportunites and collaborations. Feel free to reach out to me if you'd like to connect, collaborate, or just have a chat.",
    "You can find me on Github or LinkedIn, in previous site. ",
    "Lets code... "
];

let currentIndex = 0;

function displayNextDescription() {
    if(currentIndex < descriptions.length){
        const description = descriptions[currentIndex];
        const paragraph = document.createElement("p");
        paragraph.textContent = description;
        paragraph.classList.add("fadeIn");
        descriptionContainer.appendChild(paragraph);
        currentIndex++;
        setTimeout(displayNextDescription, 2000);
    }
}

document.getElementById("backbutton").addEventListener("click", () => {
    window.history.back();

});

window.onload = function () {
    displayNextDescription();

}