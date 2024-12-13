import 'dart:convert';

import 'package:http/http.dart' as http;

class AuthRemoteRepository {
  final uri = 'http://10.0.2.2:8000/auth';
  Future<void> signup({
    required String name,
    required String email,
    required String password,
  }) async {
    try {
      final respose = await http.post(
        Uri.parse(
          "$uri/signup",
        ),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(
          {
            'name': name,
            'email': email,
            'password': password,
          },
        ),
      );
      print(respose.body);
      print(respose.statusCode);
    } catch (e) {
      print(e);
    }
  }

  Future<void> login({
    required String email,
    required String password,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$uri/login'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(
          {
            'email': email,
            'password': password,
          },
        ),
      );
      print(response.body);
      print(response.statusCode);
    } catch (e) {
      print(e);
    }
  }
}
