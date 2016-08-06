var app = angular.module('app', [ 'ngRoute' ]); 


app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.posts = [];
    return $http.get('/users').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.posts.push(item);
      });
    });
  }
]);