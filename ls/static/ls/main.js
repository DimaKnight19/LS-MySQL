var purchaseAmount = document.getElementById("purchase_amount"); //изначальная сумма покупки

const discount = 0.20; // 20% от суммы покупки


var pythonDataElement = document.getElementById("pythonData");
var pythonData = pythonDataElement.getAttribute("data-mydata"); //переменная содежит данные из питона для работы в js  (баланс бонусов покупателя)
var pythonDataNumber = Number(pythonData); // (баланс бонусов покупателя, число)


var maxNumberOfBonuses = document.getElementById("get_max_number_of_bonuses"); //максимальное количество бонусов, которые можно списать
var maxNumberOfBonusesNumber = Number(maxNumberOfBonuses);


var pythonPercentOfDiscountID = document.getElementById("pythonPercenOfDiscount"); // скидка покупателя
var pythonPercentOfDiscount = pythonPercentOfDiscountID.getAttribute("data-python-percent-of-discount");
var pythonPercentOfDiscountNumber = Number(pythonPercentOfDiscount);


var theNumberOfBonusesToBeDebited = document.querySelector("#the_number_of_bonuses_to_be_debited"); //количество бонусов, которые будут списаны

var sumOfPurchase = document.getElementById("sum_of_purchase"); //конечная сумма покупки
var accumulatedBonuses = document.getElementById("accumulated_bonuses"); //бонусы, которые накопятся с покупки


var calculateBonuses = document.getElementById("calculate_bonuses"); // получение кнопки "посчитать бонусы"


const currentBalance = document.getElementById("current_balance"); // баланс бонусов покупателя

var newBonuses = document.getElementById("new_bonuses"); // новый баланс бонусов покупателя
var calculateNewBonuses = document.getElementById("calculate_new_bonuses"); // получение кнопки "посчитать бонусы"


// var pythonMoneySpentID = document.getElementById("pythonMoneySpent"); // скидка покупателя
// var pythonMoneySpent = pythonPercentOfDiscountID.getAttribute("data-python-money-spent");
// var pythonMoneySpentNumber = Number(pythonMoneySpent);

// console.log(pythonMoneySpentNumber);









//Функции

// расчет максимального числа бонусов, которые можно списать

purchaseAmount.addEventListener('input', function () {
    var twentyPercent = Math.round(parseInt(purchaseAmount.value)*discount); // 20% целочислено
    console.log(twentyPercent) //проверка работы twentyPercent
    
        if (twentyPercent <= pythonDataNumber) {
            console.log(twentyPercent)
            var maxNumber1 = twentyPercent;
            document.getElementById("get_max_number_of_bonuses").value=maxNumber1; // Если 20% от изначальной суммы меньше или равно pythondataNumber, то выводим 20% 
                                                                                    

        } else if (twentyPercent > pythonDataNumber){
            console.log(pythonDataNumber)
            var maxNumber3 = pythonDataNumber;
            document.getElementById("get_max_number_of_bonuses").value=maxNumber3;

        }

        document.getElementById("accumulated_bonuses").value="";
        document.getElementById("new_bonuses").value="";
        theNumberOfBonusesToBeDebited.value="";
        sumOfPurchase.value="";
        
    });



// расчет конечной суммы продажи(покупки), бонусов, которые накопятся с продажи(покупки) и расчет нового количества бонусов покупателя
theNumberOfBonusesToBeDebited.addEventListener('input', function () {

    var numberOfBonusesToBeDebited = parseFloat(theNumberOfBonusesToBeDebited.value);
    var maxNumberOfBonusesDebited = parseFloat(maxNumberOfBonuses.value);

    // Проверяем, чтобы количество бонусов, которые будут списаны, не превышало максимальное количество
    if (numberOfBonusesToBeDebited > maxNumberOfBonusesDebited) {
        theNumberOfBonusesToBeDebited.value = maxNumberOfBonusesDebited;
        numberOfBonusesToBeDebited = maxNumberOfBonusesDebited;
    }


  
    total_price = parseFloat(purchaseAmount.value) - numberOfBonusesToBeDebited;
    sumOfPurchase.value = total_price; // расчет конечной суммы продажи(покупки)


    if (pythonPercentOfDiscountNumber == 2){
        
        var numberBon=parseInt(sumOfPurchase.value)*0.02; // расчет бонусов, которые накопятся с продажи(покупки)
        roundNumberBon=Math.round(numberBon); // расчет бонусов, которые накопятся с продажи(покупки)



        document.getElementById("accumulated_bonuses").value=roundNumberBon; // расчет бонусов, которые накопятся с продажи(покупки)

        var numOfNewBon=pythonDataNumber-parseInt(theNumberOfBonusesToBeDebited.value)+roundNumberBon; // расчет нового количества бонусов покупателя
        document.getElementById("new_bonuses").value=numOfNewBon;

    } else if (pythonPercentOfDiscountNumber == 3){

        var numberBon=parseInt(sumOfPurchase.value)*0.03;
        roundNumberBon=Math.round(numberBon);


        document.getElementById("accumulated_bonuses").value=roundNumberBon;

        var numOfNewBon=pythonDataNumber-parseInt(theNumberOfBonusesToBeDebited.value)+roundNumberBon; 
        document.getElementById("new_bonuses").value=numOfNewBon;


    } else if (pythonPercentOfDiscountNumber == 5){

        var numberBon=parseInt(sumOfPurchase.value)*0.05;
        roundNumberBon=Math.round(numberBon);



        document.getElementById("accumulated_bonuses").value=roundNumberBon;

        var numOfNewBon=pythonDataNumber-parseInt(theNumberOfBonusesToBeDebited.value)+roundNumberBon; 
        document.getElementById("new_bonuses").value=numOfNewBon;

    } else if (pythonPercentOfDiscountNumber == 7){

        var numberBon=parseInt(sumOfPurchase.value)*0.07;
        roundNumberBon=Math.round(numberBon);



        document.getElementById("accumulated_bonuses").value=roundNumberBon;

        var numOfNewBon=pythonDataNumber-parseInt(theNumberOfBonusesToBeDebited.value)+roundNumberBon; 
        document.getElementById("new_bonuses").value=numOfNewBon;

    } else if (pythonPercentOfDiscountNumber == 10){

        var numberBon=parseInt(sumOfPurchase.value)*0.1;
        roundNumberBon=Math.round(numberBon);



        document.getElementById("accumulated_bonuses").value=roundNumberBon;

        var numOfNewBon=pythonDataNumber-parseInt(theNumberOfBonusesToBeDebited.value)+roundNumberBon; 
        document.getElementById("new_bonuses").value=numOfNewBon;
    }


    });

// функция вычисления оставшейся суммы до следующего уровня бонусов

function calculateNextDiscountSpending() {
    var pythonMoneySpentID = document.getElementById("pythonMoneySpent");
    var pythonMoneySpent = pythonMoneySpentID.getAttribute("data-python-money-spent");
    var pythonMoneySpentNumber = parseFloat(pythonMoneySpent);
    
    var currentDiscountLevel = Math.floor(pythonMoneySpentNumber / 10000); // Текущий уровень скидки
    var amountSpentAboveCurrentDiscount = pythonMoneySpentNumber - (currentDiscountLevel * 10000); // Сумма потраченная сверх текущего уровня скидки
    var remainingToNextDiscount = 10001 - amountSpentAboveCurrentDiscount; // Оставшаяся сумма до следующего уровня скидки
    
    if (remainingToNextDiscount === 0) {
        remainingToNextDiscount = 10001; // Если уже достигнут новый уровень скидки, пересчитываем до следующего
    }
    
    return remainingToNextDiscount.toFixed(1); // Преобразование к числу с плавающей запятой с двумя знаками после запятой
}

var moneyNeededForNextDiscount = calculateNextDiscountSpending();
document.getElementById("nextDiscountAmount").textContent = moneyNeededForNextDiscount;