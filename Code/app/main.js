document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/updates/real-time')
        .then(response => response.json())
        .then(data => {
            const tradeVolumeChart = new Chart(document.getElementById('tradeVolumeChart'), {
                type: 'line',
                data: {
                    labels: data.tradeLabels,
                    datasets: [{
                        label: 'Trade Volume',
                        data: data.tradeVolumes,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)'
                    }]
                }
            });

            const inventoryChart = new Chart(document.getElementById('inventoryChart'), {
                type: 'bar',
                data: {
                    labels: data.inventoryLabels,
                    datasets: [{
                        label: 'Inventory Levels',
                        data: data.inventoryLevels,
                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                        borderColor: 'rgba(153, 102, 255, 1)'
                    }]
                }
            });
        });
});
