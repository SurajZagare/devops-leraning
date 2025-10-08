<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Visual Guide to Git Commands</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f4f8;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 400px;
            }
        }
        .flow-step {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            font-weight: 600;
            min-height: 80px;
        }
        .flow-arrow {
            font-size: 2.5rem;
            color: #118AB2;
            margin: 0 1rem;
            transform: rotate(90deg);
        }
        @media (min-width: 768px) {
            .flow-arrow {
                transform: rotate(0deg);
            }
        }
    </style>
</head>
<body class="text-[#073B4C]">

    <div class="container mx-auto p-4 md:p-8 max-w-7xl">

        <header class="text-center mb-12 md:mb-16">
            <h1 class="text-4xl md:text-6xl font-bold text-[#073B4C] mb-2">🐙 A Visual Guide to Git Commands</h1>
            <p class="text-lg md:text-xl text-[#118AB2]">Your ultimate interactive cheatsheet for mastering Git.</p>
        </header>

        <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

            <section class="md:col-span-2 lg:col-span-3 bg-white rounded-lg shadow-lg p-6 md:p-8">
                <h2 class="text-2xl font-bold mb-4">The Daily Git Workflow</h2>
                <p class="mb-6 text-gray-600">This is the fundamental process every developer follows. It's a simple loop of checking the status of your project, adding your changes to a "staging area," and then permanently saving them with a descriptive commit message.</p>
                <div class="flex flex-col md:flex-row items-center justify-center space-y-4 md:space-y-0 md:space-x-4">
                    <div class="flow-step bg-[#FFD166] text-[#073B4C]">Workspace</div>
                    <div class="flow-arrow font-mono">&rarr;</div>
                    <div class="flex flex-col items-center">
                        <code class="text-sm font-semibold text-[#118AB2]">git add .</code>
                        <div class="flow-step bg-[#06D6A0] text-white mt-1">Staging Area</div>
                    </div>
                    <div class="flow-arrow font-mono">&rarr;</div>
                     <div class="flex flex-col items-center">
                        <code class="text-sm font-semibold text-[#118AB2]">git commit -m "..."</code>
                        <div class="flow-step bg-[#118AB2] text-white mt-1">Local Repository</div>
                    </div>
                </div>
            </section>
            
            <section class="bg-white rounded-lg shadow-lg p-6 md:p-8">
                <h2 class="text-2xl font-bold mb-4">Command Category Breakdown</h2>
                <p class="mb-6 text-gray-600">Git has a rich command set. This chart shows how commands are distributed across different functions, highlighting that collaboration (Branching & Remotes) is a core part of the ecosystem.</p>
                <div class="chart-container">
                    <canvas id="commandCategoriesChart"></canvas>
                </div>
            </section>
            
            <section class="bg-white rounded-lg shadow-lg p-6 md:p-8">
                <h2 class="text-2xl font-bold mb-4">The Core Command Loop</h2>
                <p class="mb-6 text-gray-600">While there are many commands, a few make up the vast majority of daily use. This shows the commands from the "Shortcut Summary" which form the essential toolkit for most developers.</p>
                <div class="chart-container">
                    <canvas id="coreCommandsChart"></canvas>
                </div>
            </section>

            <section class="lg:col-span-1 bg-white rounded-lg shadow-lg p-6 md:p-8 flex flex-col items-center justify-center text-center">
                <h2 class="text-2xl font-bold mb-4">Stashing: A Lifesaver</h2>
                <p class="mb-6 text-gray-600">Need to switch branches but aren't ready to commit? `git stash` temporarily shelves your changes so you can come back to them later. It's like a clipboard for your work-in-progress.</p>
                 <div class="text-8xl mb-4">📥</div>
                <code class="text-xl font-bold p-3 bg-gray-100 rounded-lg text-[#FF6B6B]">git stash pop</code>
                <p class="mt-4 text-gray-600">...to bring them right back!</p>
            </section>

            <section class="md:col-span-2 lg:col-span-3 bg-white rounded-lg shadow-lg p-6 md:p-8">
                <h2 class="text-2xl font-bold mb-4">Local vs. Remote: The Collaboration Hub</h2>
                <p class="mb-6 text-gray-600">Git's power shines in teamwork. Your local repository is your private workspace. The remote repository (like GitHub) is the shared, central source of truth. These commands sync your work with the team.</p>
                 <div class="grid grid-cols-1 md:grid-cols-3 items-center gap-4 text-center">
                    <div class="p-6 bg-blue-50 border-2 border-dashed border-[#118AB2] rounded-lg">
                        <h3 class="text-xl font-semibold">💻 Local Repo</h3>
                        <p class="text-sm text-gray-500">Your machine</p>
                    </div>
                    <div class="flex flex-col items-center justify-around h-full">
                       <div class="w-full text-center">
                            <p class="font-semibold">Share your work &rarr;</p>
                            <code class="text-lg font-bold text-[#06D6A0]">git push</code>
                        </div>
                        <div class="w-full text-center mt-4">
                            <p class="font-semibold">&larr; Get team updates</p>
                            <code class="text-lg font-bold text-[#FFD166]">git pull</code>
                        </div>
                    </div>
                    <div class="p-6 bg-green-50 border-2 border-dashed border-[#06D6A0] rounded-lg">
                        <h3 class="text-xl font-semibold">☁️ Remote Repo</h3>
                        <p class="text-sm text-gray-500">GitHub / GitLab</p>
                    </div>
                </div>
            </section>
            
            <section class="md:col-span-2 lg:col-span-3 bg-white rounded-lg shadow-lg p-6 md:p-8">
                 <h2 class="text-2xl font-bold mb-4">Undoing Changes: Choose Your Weapon Wisely</h2>
                 <p class="mb-6 text-gray-600">Making mistakes is part of coding. Git provides several ways to undo them, ranging from safe, reversible actions to destructive, permanent changes. Understanding the difference is critical.</p>
                 <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="border-l-8 border-[#06D6A0] bg-green-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold">Safe: `git revert`</h3>
                        <p class="mt-2 text-gray-700">Creates a <span class="font-semibold">new commit</span> that undoes a previous one. It's the safest method for public branches as it doesn't rewrite history.</p>
                    </div>
                    <div class="border-l-8 border-[#FFD166] bg-yellow-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold">Careful: `git restore` / `git reset`</h3>
                        <p class="mt-2 text-gray-700">Discards local changes or unstages files. It affects your working directory or staging area, but not your commit history.</p>
                    </div>
                     <div class="border-l-8 border-[#FF6B6B] bg-red-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold">Dangerous: `git reset --hard`</h3>
                        <p class="mt-2 text-gray-700"><span class="font-semibold">Deletes commits and changes</span> permanently. Avoid on shared branches as it rewrites history, which can cause major issues for collaborators.</p>
                    </div>
                 </div>
            </section>

        </main>

        <footer class="text-center mt-12 md:mt-16 text-gray-500">
            <p>Infographic created with Chart.js and Tailwind CSS.</p>
        </footer>

    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {

            const wrapLabel = (label, maxLength = 16) => {
                if (label.length <= maxLength) {
                    return label;
                }
                const words = label.split(' ');
                const lines = [];
                let currentLine = '';
                for (const word of words) {
                    if ((currentLine + ' ' + word).trim().length > maxLength) {
                        lines.push(currentLine.trim());
                        currentLine = word;
                    } else {
                        currentLine = (currentLine + ' ' + word).trim();
                    }
                }
                if (currentLine) {
                    lines.push(currentLine.trim());
                }
                return lines;
            };

            const tooltipTitleCallback = (tooltipItems) => {
                const item = tooltipItems[0];
                let label = item.chart.data.labels[item.dataIndex];
                if (Array.isArray(label)) {
                    return label.join(' ');
                }
                return label;
            };
            
            const sharedChartOptions = {
                 maintainAspectRatio: false,
                 responsive: true,
                 plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            font: {
                                family: "'Inter', sans-serif"
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            title: tooltipTitleCallback
                        }
                    }
                }
            };
            
            const energeticPalette = ['#118AB2', '#06D6A0', '#FFD166', '#FF6B6B', '#073B4C', '#EE6C4D'];

            const ctxCategories = document.getElementById('commandCategoriesChart')?.getContext('2d');
            if (ctxCategories) {
                const categoryLabels = [
                    'Basic Setup', 'Starting a Repository', 'Staging and Committing', 
                    'Branching and Merging', 'Working with Remote Repos', 'Viewing History', 
                    'Undoing Changes', 'Tagging', 'Stashing', 'Advanced Commands'
                ].map(label => wrapLabel(label));
                
                new Chart(ctxCategories, {
                    type: 'bar',
                    data: {
                        labels: categoryLabels,
                        datasets: [{
                            label: 'Number of Commands',
                            data: [5, 2, 5, 6, 7, 5, 5, 5, 5, 5],
                            backgroundColor: energeticPalette,
                            borderColor: energeticPalette.map(c => c + 'B3'),
                            borderWidth: 1
                        }]
                    },
                    options: {
                        ...sharedChartOptions,
                        indexAxis: 'y',
                        scales: {
                            x: {
                                beginAtZero: true,
                                ticks: {
                                    stepSize: 1
                                }
                            }
                        },
                        plugins: {
                           ...sharedChartOptions.plugins,
                           legend: { display: false }
                        }
                    }
                });
            }

            const ctxCore = document.getElementById('coreCommandsChart')?.getContext('2d');
            if (ctxCore) {
                new Chart(ctxCore, {
                    type: 'doughnut',
                    data: {
                        labels: ['git add .', 'git commit', 'git push', 'git pull', 'git checkout -b', 'git merge'],
                        datasets: [{
                            label: 'Core Commands',
                            data: [20, 20, 20, 15, 15, 10],
                             backgroundColor: energeticPalette,
                             hoverOffset: 4
                        }]
                    },
                    options: {
                         ...sharedChartOptions
                    }
                });
            }

        });
    </script>
</body>
</html>
