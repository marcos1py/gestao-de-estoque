$('#id_importado').removeClass('form-control');
<script>
    document.addEventListener('DOMContentLoaded', function () {
        var ctx = document.getElementById('faturamento-chart').getContext('2d');
        
        var faturamentoData = {
            labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            datasets: [{
                label: 'Faturamento Mensal',
                data: {{ faturamento_mensal|safe }},
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
            }],
        };
        
        var faturamentoChart = new Chart(ctx, {
            type: 'line',
            data: faturamentoData,
            options: {
                scales: {
                    x: [{
                        grid: {
                            display: false,
                        },
                    }],
                    y: [{
                        ticks: {
                            beginAtZero: true,
                        },
                    }],
                },
                legend: {
                    display: false,
                },
            },
        });
    });
</script>
