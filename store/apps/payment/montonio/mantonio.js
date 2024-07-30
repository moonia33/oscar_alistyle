$(document).ready(function () {
    $('#country-select').change(function () {
        var selectedCountry = $(this).val();
        loadPaymentMethods(selectedCountry);
    });

    function loadPaymentMethods(countryCode) {
        // Pakeiskite URL į jūsų tinkamą endpoint
        var url = '/get_payment_methods/' + countryCode + '/';

        $.ajax({
            url: url,
            method: 'GET',
            success: function (data) {
                renderPaymentMethods(data);
            },
            error: function (xhr, status, error) {
                console.error('Klaida gaunant mokėjimo būdus:', status, error);
            }
        });
    }

    function renderPaymentMethods(data) {
        var container = $('#payment-methods-container');
        container.empty();

        if (data.paymentMethods.length === 0) {
            container.append('<p>Šioje šalyje nėra galimų mokėjimo būdų.</p>');
            return;
        }

        $.each(data.paymentMethods, function (index, method) {
            var methodHtml = `
                <div class="payment-method">
                    <img src="${method.logoUrl}" alt="${method.name}">
                    <span>${method.name}</span>
                </div>`;
            container.append(methodHtml);
        });
    }

    // Pirma užkrova
    loadPaymentMethods($('#country-select').val());
});
