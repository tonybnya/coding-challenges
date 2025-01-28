const challenges = [
  {
    id: 1,
    title: "Task List",
    stack: ["React", "Tailwind"],
    description:
      "Create a simple React component that displays a list of tasks. Each task has a name and a completion status. The component should allow the user to toggle the progress status of each task.",
    snippet: `import React, { useState } from 'react';
  
  const tasks = [
      { name: "Task 1", completed: false },
      { name: "Task 2", completed: true },
      { name: "Task 3", completed: false }
  ];
  
  const TaskList = () => {
      // Your code here
  }
  
  export default TaskList;`,
    completed: false,
  },
  {
    id: 2,
    title: "Counter App",
    stack: ["React"],
    description:
      "Create a React component that displays a counter with buttons to increment and decrement the count.",
    snippet: `import React, { useState } from 'react';
  
  const Counter = () => {
      // Your code here
  }
  
  export default Counter;`,
    completed: false,
  },
  {
    id: 3,
    title: "Todo List",
    stack: ["React", "Tailwind"],
    description:
      "Build a Todo List app where users can add, delete, and mark tasks as completed.",
    snippet: `import React, { useState } from 'react';
  
  const TodoList = () => {
      // Your code here
  }
  
  export default TodoList;`,
    completed: false,
  },
  {
    id: 4,
    title: "Form Validation",
    stack: ["React"],
    description:
      "Create a form with fields for name, email, and password. Add validation to ensure all fields are filled and the email is valid.",
    snippet: `import React, { useState } from 'react';
  
  const Form = () => {
      // Your code here
  }
  
  export default Form;`,
    completed: false,
  },
  {
    id: 5,
    title: "Fetch Data from API",
    stack: ["React"],
    description:
      "Fetch data from a public API (e.g., JSONPlaceholder) and display it in a list.",
    snippet: `import React, { useEffect, useState } from 'react';
  
  const FetchData = () => {
      // Your code here
  }
  
  export default FetchData;`,
    completed: false,
  },
  {
    id: 6,
    title: "Dark Mode Toggle",
    stack: ["React", "Tailwind"],
    description:
      "Implement a dark mode toggle switch that changes the theme of the app.",
    snippet: `import React, { useState } from 'react';
  
  const DarkModeToggle = () => {
      // Your code here
  }
  
  export default DarkModeToggle;`,
    completed: false,
  },
  {
    id: 7,
    title: "Pagination",
    stack: ["React"],
    description:
      "Create a pagination component that displays a limited number of items per page and allows navigation between pages.",
    snippet: `import React, { useState } from 'react';
  
  const Pagination = ({ data }) => {
      // Your code here
  }
  
  export default Pagination;`,
    completed: false,
  },
  {
    id: 8,
    title: "Search Filter",
    stack: ["React"],
    description:
      "Build a search filter that dynamically filters a list of items based on user input.",
    snippet: `import React, { useState } from 'react';
  
  const SearchFilter = ({ data }) => {
      // Your code here
  }
  
  export default SearchFilter;`,
    completed: false,
  },
  {
    id: 9,
    title: "Modal Component",
    stack: ["React"],
    description:
      "Create a reusable modal component that can be triggered by a button click.",
    snippet: `import React, { useState } from 'react';
  
  const Modal = () => {
      // Your code here
  }
  
  export default Modal;`,
    completed: false,
  },
  {
    id: 10,
    title: "Accordion Component",
    stack: ["React"],
    description:
      "Build an accordion component that allows users to expand and collapse sections of content.",
    snippet: `import React, { useState } from 'react';
  
  const Accordion = ({ items }) => {
      // Your code here
  }
  
  export default Accordion;`,
    completed: false,
  },
  {
    id: 11,
    title: "Carousel Component",
    stack: ["React"],
    description:
      "Create a carousel component that cycles through a set of images or content.",
    snippet: `import React, { useState } from 'react';
  
  const Carousel = ({ items }) => {
      // Your code here
  }
  
  export default Carousel;`,
    completed: false,
  },
  {
    id: 12,
    title: "Infinite Scroll",
    stack: ["React"],
    description:
      "Implement an infinite scroll feature that loads more data as the user scrolls down the page.",
    snippet: `import React, { useState, useEffect } from 'react';
  
  const InfiniteScroll = () => {
      // Your code here
  }
  
  export default InfiniteScroll;`,
    completed: false,
  },
  {
    id: 13,
    title: "Drag and Drop",
    stack: ["React"],
    description:
      "Build a drag-and-drop interface where users can reorder items in a list.",
    snippet: `import React from 'react';
  
  const DragAndDrop = () => {
      // Your code here
  }
  
  export default DragAndDrop;`,
    completed: false,
  },
  {
    id: 14,
    title: "Authentication Flow",
    stack: ["React"],
    description:
      "Create a simple authentication flow with login and signup forms using React and a mock API.",
    snippet: `import React, { useState } from 'react';
  
  const AuthFlow = () => {
      // Your code here
  }
  
  export default AuthFlow;`,
    completed: false,
  },
  {
    id: 15,
    title: "Responsive Navbar",
    stack: ["React", "Tailwind"],
    description:
      "Build a responsive navbar that collapses into a hamburger menu on smaller screens.",
    snippet: `import React, { useState } from 'react';
  
  const Navbar = () => {
      // Your code here
  }
  
  export default Navbar;`,
    completed: false,
  },
  {
    id: 16,
    title: "Quiz App",
    stack: ["React"],
    description:
      "Create a quiz app that displays questions, allows users to select answers, and shows the final score.",
    snippet: `import React, { useState } from 'react';
  
  const QuizApp = () => {
      // Your code here
  }
  
  export default QuizApp;`,
    completed: false,
  },
  {
    id: 17,
    title: "Weather App",
    stack: ["React"],
    description:
      "Build a weather app that fetches data from a weather API and displays the current weather for a given location.",
    snippet: `import React, { useState, useEffect } from 'react';
  
  const WeatherApp = () => {
      // Your code here
  }
  
  export default WeatherApp;`,
    completed: false,
  },
  {
    id: 18,
    title: "Expense Tracker",
    stack: ["React"],
    description:
      "Create an expense tracker app where users can add, edit, and delete expenses.",
    snippet: `import React, { useState } from 'react';
  
  const ExpenseTracker = () => {
      // Your code here
  }
  
  export default ExpenseTracker;`,
    completed: false,
  },
  {
    id: 19,
    title: "Countdown Timer",
    stack: ["React"],
    description:
      "Build a countdown timer that counts down from a specified time and displays the remaining time.",
    snippet: `import React, { useState, useEffect } from 'react';
  
  const CountdownTimer = () => {
      // Your code here
  }
  
  export default CountdownTimer;`,
    completed: false,
  },
  {
    id: 20,
    title: "Random Quote",
    stack: ["React"],
    description:
      "Create a random quote generator that fetches and displays a new quote when a button is clicked.",
    snippet: `import React, { useState } from 'react';
  
  const QuoteGenerator = () => {
      // Your code here
  }
  
  export default QuoteGenerator;`,
    completed: false,
  },
  {
    id: 21,
    title: "Markdown Previewer",
    stack: ["React"],
    description:
      "Build a markdown previewer that allows users to write markdown text and see a live preview of the rendered output.",
    snippet: `import React, { useState } from 'react';
  
  const MarkdownPreviewer = () => {
      // Your code here
  }
  
  export default MarkdownPreviewer;`,
    completed: false,
  },
  {
    id: 22,
    title: "Tic Tac Toe Game",
    stack: ["React"],
    description:
      "Create a Tic Tac Toe game where two players can take turns and the game declares a winner or a draw.",
    snippet: `import React, { useState } from 'react';
  
  const TicTacToe = () => {
      // Your code here
  }
  
  export default TicTacToe;`,
    completed: false,
  },
  {
    id: 23,
    title: "Memory Game",
    stack: ["React"],
    description:
      "Build a memory game where users flip cards to find matching pairs.",
    snippet: `import React, { useState } from 'react';
  
  const MemoryGame = () => {
      // Your code here
  }
  
  export default MemoryGame;`,
    completed: false,
  },
  {
    id: 24,
    title: "Calculator",
    stack: ["React"],
    description:
      "Create a simple calculator that can perform basic arithmetic operations.",
    snippet: `import React, { useState } from 'react';
  
  const Calculator = () => {
      // Your code here
  }
  
  export default Calculator;`,
    completed: false,
  },
  {
    id: 25,
    title: "URL Shortener",
    stack: ["React"],
    description:
      "Build a URL shortener app that takes a long URL and returns a shortened version.",
    snippet: `import React, { useState } from 'react';
  
  const UrlShortener = () => {
      // Your code here
  }
  
  export default UrlShortener;`,
    completed: false,
  },
  {
    id: 26,
    title: "Blog App",
    stack: ["React"],
    description:
      "Create a simple blog app where users can view, add, and delete blog posts.",
    snippet: `import React, { useState } from 'react';
  
  const BlogApp = () => {
      // Your code here
  }
  
  export default BlogApp;`,
    completed: false,
  },
  {
    id: 27,
    title: "E-commerce Product",
    // title: "E-commerce Product Page",
    stack: ["React", "Tailwind"],
    description:
      "Build a product page for an e-commerce site with a product image, description, and add-to-cart button.",
    snippet: `import React from 'react';
  
  const ProductPage = () => {
      // Your code here
  }
  
  export default ProductPage;`,
    completed: false,
  },
  {
    id: 28,
    title: "Chat App",
    stack: ["React"],
    description:
      "Create a simple chat app where users can send and receive messages in real-time.",
    snippet: `import React, { useState } from 'react';
  
  const ChatApp = () => {
      // Your code here
  }
  
  export default ChatApp;`,
    completed: false,
  },
  {
    id: 29,
    title: "Portfolio Website",
    stack: ["React", "Tailwind"],
    description:
      "Build a personal portfolio website with sections for about, projects, and contact information.",
    snippet: `import React from 'react';
  
  const Portfolio = () => {
      // Your code here
  }
  
  export default Portfolio;`,
    completed: true,
  },
  {
    id: 30,
    title: "Movie Search App",
    stack: ["React"],
    description:
      "Create a movie search app that fetches data from a movie API and allows users to search for movies by title.",
    snippet: `import React, { useState, useEffect } from 'react';
  
  const MovieSearch = () => {
      // Your code here
  }
  
  export default MovieSearch;`,
    completed: false,
  },
];

export default challenges;
