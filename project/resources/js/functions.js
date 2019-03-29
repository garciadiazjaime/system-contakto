/*
	Author: Mint IT Media
*/
var folder = '/';

$(document).ready(function() {
    var page = get_currentpage();

    if (page.indexOf('exito') != -1) {
        showMSG('msg', 'Tu operación se realizó con éxito', 'alert alert-success text-center');
    } else if (page.indexOf('error') != -1) {
        showMSG('msg', 'Tu operación no pudo ser realizada, favor de intentar de nuevo', 'alert alert-danger');
    }

    $('#navigation_tabs a').click(function(e) {
        e.preventDefault()
        $(this).tab('show')
    });

    $('input, select').keypress(function(event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });

    $('#id_investigacion-fecha_recibido, #id_fecha_entrevista, #id_trayectoria-aportaciones_fecha_inicial, #id_trayectoria-aportaciones_fecha_final, #id_trayectoria-periodo_alta, #id_trayectoria-periodo_baja, #id_deudas-0-fecha_otorgamiento, #id_deudas-1-fecha_otorgamiento').each(function() {
        if (typeof $(this) != 'undefined') {
            $(this).datepicker({
                format: 'dd/mm/yyyy'
            })
        }
    });

    if ($('.datepicker').length) {
        $('.datepicker').each(function() {
            if (typeof $(this).split != 'undefined') {
                $(this).datepicker({
                    format: 'dd/mm/yyyy'
                });
            }
        })
    };

    $('#id_hora_entrevista').timepicker({
        'timeFormat': 'G:i'
    });

    $('.timepicker').timepicker({
        'timeFormat': 'G:i'
    });

    $('.phone')
        .keydown(function(e) {
            var key = e.charCode || e.keyCode || 0;
            $phone = $(this);

            // Auto-format- do not expose the mask as the user begins to type
            if (key !== 8 && key !== 9) {
                if ($phone.val().length === 0) {
                    $phone.val('(');
                }
                if ($phone.val().length === 1 && $phone.val().indexOf('(') == -1) {
                    $phone.val('(' + $phone.val());
                }
                if ($phone.val().length === 4) {
                    $phone.val($phone.val() + ')');
                }
                if ($phone.val().length === 5) {
                    $phone.val($phone.val() + ' ');
                }
                if ($phone.val().length === 9) {
                    $phone.val($phone.val() + '-');
                }
            }

            // Allow numeric (and tab, backspace, delete) keys only
            return (key == 8 ||
                key == 9 ||
                key == 46 ||
                (key >= 48 && key <= 57) ||
                (key >= 96 && key <= 105));
        })

    .bind('focus click', function() {
        $phone = $(this);

        if ($phone.val().length === 0) {
            $phone.val('(');
        } else {
            var val = $phone.val();
            // Ensure cursor remains at the end
            $phone.val('').val(val);
        }
    })

    .blur(function() {
        $phone = $(this);

        if ($phone.val() === '(') {
            $phone.val('');
        }
    });

    $('.btn_eliminar').click(function() {
        if (confirm('Seguro que deseas eliminar?')) {
            return true;
        }
        return false;
    })

    $('.btn_quitar_factura').click(function() {
        if (confirm('Seguro que deseas quitar el # de factura?')) {
            return true;
        }
        return false;
    })

    $('.btn_agregrar_factura').click(function() {
        if (confirm('Seguro que deseas agregar el # de factura?')) {
            return true;
        }
        return false;
    })

    $('.missing-form-control input[type=text], .missing-form-control input[type=number]').addClass('form-control');

    $(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
        event.preventDefault();
        $(this).ekkoLightbox();
    });

    formatCurrencyFields();

});

function get_currentpage() {
    var loc = window.location;
    var loc_ref_sinfiltros = loc.href.indexOf('?') > -1 ? loc.href.substring(0, loc.href.indexOf('?')) : loc.href
    p = loc_ref_sinfiltros.substring(loc.href.indexOf(loc.host) + loc.host.length + folder.length);
    if (p == '') p = '/investigaciones';
    return p;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        var csrftoken = getCookie('csrftoken');
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function showMSG(id, msg, custom_class) {
    $('#' + id).css({
        'opacity': '0',
        'position': 'absolute',
        'z-index': '10',
        'width': '100%'
    }).removeClass().addClass(custom_class).text(msg).animate({
        opacity: 1
    }, 500, function() {
        removeMSG(id);
    });
}

function removeMSG(id) {
    setTimeout(function() {
        $('#' + id).animate({
                opacity: 0
            },
            1000,
            function() {
                $('#' + id).removeClass().text('').css({
                    'position': 'initial',
                    'z-index': 'initial',
                    'width': 'initial'
                });
            });
    }, 3000);
}

/*
 * Function to calculate Age based in date of birth.
 * extracted from: http://www.romcartridge.com/2010/01/javascript-function-to-calculate-age.html
 * @param {integer} birthMonth
 * @param {integer} birthDay
 * @param {integer} birthYear
 * @return {integer} age
 */
function calculateAge(birthMonth, birthDay, birthYear) {
    todayDate = new Date();
    todayYear = todayDate.getFullYear();
    todayMonth = todayDate.getMonth();
    todayDay = todayDate.getDate();
    age = todayYear - birthYear;

    if (todayMonth < birthMonth - 1) {
        age--;
    }

    if (birthMonth - 1 == todayMonth && todayDay < birthDay) {
        age--;
    }
    return age;
}

/*
	function to give money format $XX,XXX.XX to all fields with custom_money_format class, that class is assigned in the BE
*/
function formatCurrencyFields() {
    var fields = $('.custom_money_format');
    fields.map(function(index) {
        // clean the value from DB and get a "real" number 
        var value = fields[index].value.match(/[\d,]+(\.[\d]+)*/gi) ? fields[index].value.match(/[\d,]+(\.[\d]+)*/gi).toString().replace(/,/g, '') : null;
        if (value) {
            // if value passes our regext then we call customFormatMoney to show number on the rirght format
            fields[index].value = customFormatMoney(value, 2, '.', ',');
        }
    })
}

/*
	function got it from: http://stackoverflow.com/questions/2116558/fastest-method-to-replace-all-instances-of-a-character-in-a-string
	adapt 'n' parameter to receive value to format
	@n {integer} n value to format
	@c {integer} c point fixed number, helps to know how many decimels to show
	@d {char} d fixed symbol to show
	@t {char} t thousand symbol
	@return {string} format value
*/
customFormatMoney = function(n, c, d, t) {
    var c = isNaN(c = Math.abs(c)) ? 2 : c,
        d = d == undefined ? "." : d,
        t = t == undefined ? "," : t,
        s = n < 0 ? "-" : "",
        i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "",
        j = (j = i.length) > 3 ? j % 3 : 0;
    return '$' + s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};