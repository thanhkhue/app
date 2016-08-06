var app = angular.module('app', [ 'ngRoute' ]); 


app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.places_list = [];
    return $http.get('/places').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.places_list.push(item);
      });
    });
  }
]);