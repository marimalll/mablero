// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');
    // И через 7 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            // Просто скрываем с анимацией
            notification.fadeOut(400, function() {
                $(this).remove(); // Удаляем из DOM после скрытия
            });
        }, 3000);
    }

    // Также обрабатываем динамические уведомления
    var jqNotification = $('#jq-notification');
    if (jqNotification.length > 0) {
        setTimeout(function () {
            jqNotification.fadeOut(400, function() {
                $(this).remove();
            });
        }, 3000);
    }

    // При клике по значку корзины открываем всплывающее(модальное) окно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');
        $('#exampleModal').modal('show');
    });

    // Собыите клик по кнопке закрыть окна корзины
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});