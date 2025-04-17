document.getElementById('task-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const task = {
      title: document.getElementById('title').value,
      description: document.getElementById('description').value,
      deadline: document.getElementById('deadline').value,
      priority: document.getElementById('priority').value
    };
    
    // Save to localStorage (mocking backend for now)
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.push(task);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    
    alert('Tarefa salva com sucesso!');
    displayTasks();
  });
  
  function displayTasks() {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = tasks.map(task => `
      <div>
        <h3>${task.title} [${task.priority}]</h3>
        <p>${task.description}</p>
        <p>Prazo: ${task.deadline}</p>
      </div>
    `).join('');
  }
  
  displayTasks();